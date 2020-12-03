from maya import OpenMaya, cmds, OpenMayaUI
import math
import pymel.core as p


def returnActiveCamera():
    view = OpenMayaUI.M3dView.active3dView()
    dagCamera = OpenMaya.MDagPath()
    view.getCamera(dagCamera)
    return OpenMaya.MFnDagNode(dagCamera.transform()).name()


def RayIntersect(point, direction):
    sList = OpenMaya.MSelectionList()
    nodes = cmds.ls(tr=True)
    meshes = []
    for node in nodes:
        shapes = cmds.listRelatives(node, shapes=True, typ="mesh")
        if shapes:
            meshes.append(node)
            sList.add(node)
    selIt = OpenMaya.MItSelectionList(sList)
    result = []
    while not selIt.isDone():
        item = OpenMaya.MDagPath()
        selIt.getDagPath(item)
        item.extendToShape()
        fnMesh = OpenMaya.MFnMesh(item)
        raySource = OpenMaya.MFloatPoint(point[0], point[1], point[2], 1.0)
        rayDir = OpenMaya.MFloatVector(
            direction[0], direction[1], direction[2])
        faceIds = None
        triIds = None
        idsSorted = False
        testBothDirections = True
        worldSpace = OpenMaya.MSpace.kWorld
        maxParam = 999
        accelParams = None
        sortHits = True
        hitPoints = OpenMaya.MFloatPointArray()
        hitRayParams = OpenMaya.MFloatArray()
        hitFaces = OpenMaya.MIntArray()
        hitTris = None
        hitBarys1 = None
        hitBarys2 = None
        tolerance = 0.0001
        fnMesh.allIntersections(raySource, rayDir, faceIds, triIds, idsSorted, worldSpace, maxParam,
                                testBothDirections, accelParams, sortHits, hitPoints, hitRayParams, hitFaces,
                                hitTris, hitBarys1, hitBarys2, tolerance)
        try:
            result.append([hitPoints[0].x, hitPoints[0].y, hitPoints[0].z])
        except:
            print('None')
        selIt.next()
    return result


def findShortestDistance(original, arrOfPositions):

    shortestDistance = float('inf')
    position = [0, 0, 0]
    for pos in arrOfPositions:
        dx = original[0] - pos[0]
        dy = original[1] - pos[1]
        dz = original[2] - pos[2]
        newDistance = math.sqrt(dx*dx + dy*dy + dz*dz)
        if (shortestDistance > newDistance):
            shortestDistance = newDistance
            position = pos

    return position


def getVectorBetweenTwoPoints(start, end):
    startPosition = p.xform(start, q=True, ws=True, t=True)
    startPosition = p.datatypes.Point(startPosition)
    endPosition = p.xform(end, q=True, ws=True, t=True)
    endPosition = p.datatypes.Point(endPosition)
    return p.datatypes.Vector(endPosition - startPosition)


def run(loc):
    cam = returnActiveCamera()
    wsTransform = cmds.xform(cam, q=1, ws=1, rp=1, a=1)
    direction = getVectorBetweenTwoPoints(cam, loc)
    intersections = RayIntersect(wsTransform, direction)
    if(len(intersections) == 0):
        print('No snappy for {0}'.format(loc))
    if(len(intersections) == 1):
        cmds.move(intersections[0][0], intersections[0]
                  [1], intersections[0][2], loc, absolute=True)
    if(len(intersections) > 1):
        locPosition = p.xform(loc, q=True, ws=True, t=True)
        shortDis = findShortestDistance(locPosition, intersections)
        cmds.move(shortDis[0], shortDis[1], shortDis[2], loc, absolute=True)


def main():
    cam = returnActiveCamera()
    wsTransform = cmds.xform(cam, q=1, ws=1, rp=1, a=1)
    locators = cmds.ls(sl=True)
    for loc in locators:
        run(loc)
