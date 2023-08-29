# Usage

Download package: `pip3 install plotool`

Requires: `matplotlib`


# plotool.RealtimeDrawing

---

## Example

```python
from plotool import RealtimeDrawing
import numpy as np

drawing = RealtimeDrawing("X", "Y", "Title", 2, ["science", "ieee", "grid"])
for i in range(100):
    drawing.add_data(x=i, y=np.sin(i/10), label="sin", idx_line=1)
    drawing.add_data(x=i, y=np.cos(i/10), label="cos", idx_line=2)
    # drawing.log_xscale()    # log scale
    # drawing.log_yscale()
    drawing.plot_data()
drawing.show()
```

![plotool](https://github.com/McLinWxl/Tools/assets/104571247/fedb9015-b4f6-4976-b389-ea1781edbaf3)

