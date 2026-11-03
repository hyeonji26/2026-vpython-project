box(pos = vec(-1,0,0), texture = "https://i.postimg.cc/d0d4Jq5d/geulim2.png")
ellipsoid(pos = vec(-1, 1, 0), size = vec(3, 1, 0.5))
colors = [color.red, color.orange, color.yellow, color.green]
for i in range(4) :
    box(pos = vec(i/2-0.7, -0.3, 2), size = vec(0.1, 0.1, 0.1), color = colors[i])
box(pos = vec(0.5, 0.15, 2), size = vec(0.1, 0.27, 0.1))
