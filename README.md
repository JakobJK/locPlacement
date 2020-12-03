# locPlacement

locPlacement is a utility script for Maya, that will automatically position selected locators at the nearest geometry, from the viewpoint of the currently active camera. Helpful for especially during tracking/matchmoving

---
![locPlacement](https://i.imgur.com/ZWy5Zgb.gif)

## Usage

* Place the locPlacement.py file within your [maya scripts](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2020/ENU/Maya-Customizing/files/GUID-FA51BD26-86F3-4F41-9486-2C3CF52B9E17-htm.html) directory
* Select the locators you want to place onto Geometry
* Run the following command from the Maya Python Script Editor:

```python
import locPlacement
locPlacement.main()
```

### Author

[**Jakob Kousholt**](https://www.linkedin.com/in/jakobjk/)

### License

locPlacement is licensed under the [MIT](https://rem.mit-license.org/) License.