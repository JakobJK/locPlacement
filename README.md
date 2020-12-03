# locPlacement

locPlacement is a utility script for Maya, that will automatically position selected locators at the nearest geometry, from the viewpoint of the currently active camera. Helpful for especially during tracking/matchmoving

---

## Usage

* Place the locPlacement file within your maya scripts directory
* Select the locators you want to place onto Geometry
* Run the following command from the Maya Python Script Editor:

```python
import locPlacement
locPlacement.main()
```

## Author

[**Jakob Kousholt**](https://www.linkedin.com/in/jakejk/)

## License

locPlacement is licensed under the [MIT](https://rem.mit-license.org/) License.