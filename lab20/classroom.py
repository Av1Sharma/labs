def color_poly_helper(t, radius, n, sp):
    """
    Draws an n-sided regular colored polygon with the given radius.
    
    The polygon will centered at the current turtle position. The first vertex 
    of the polygon will be radius units along the current turtle heading. 
    
    This function is similar to draw_polygon from a4.py. It moves forward by
    radius amount without drawing. It uses an angle of 360.0/n to turn 
    90+angle/2 degrees left, orienting it on the polygon. It draws n lines
    of length 2*pi*sin(pi/n) length, turning angle left each time. When done, 
    it returns to its original position. It does this by turning 90+angle/2 
    degrees right and moving backwards by radius amount.
    
    The ONLY differences between this function and draw_polygon are (1) the
    parameter sp, (2) precondtions are enforced, and (3) the color of the 
    turtle. In particular, at each step, the the color of the turtle should be 
    alternate between "red", "cyan", and "blue", starting at "red"
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED: 
    position (x and y, within round-off errors), heading, color, speed, visible, 
    and drawmode. There is no need to restore these.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter radius: The polygon radius
    Precondition: radius is a valid side length (number >= 0)
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 1
    
    Parameter sp: The turtle speed. 
    Precondition: sp is a valid turtle speed. """
    
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(radius), report_error('radius is not a valid length', radius)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations', n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)
    
    # Remember the initial settings so they can be restored
    drawmode = t.drawmode
    heading  = t.heading
    color    = t.color
    speed    = t.speed
    
    # 2. Set the turtle speed
    t.speed = sp
    
    # Compute the exterior angle between edges
    ang = 360.0 / n
    side = 2 * radius * math.sin(math.pi / n)
    
    # Move the turtle to the starting vertex and angle
    t.drawmode = False
    t.forward(radius)
    t.left(90 + ang / 2)
    t.drawmode = drawmode
    
    # 3. Draw n lines alternating between "red", "cyan", and "blue"
    colors = ('red', 'cyan', 'blue')
    for i in range(n):
        t.color = colors[i % 3]
        t.forward(side)
        t.left(ang)
    
    # Restore the turtle to its original position, heading, color, speed, and drawmode
    t.drawmode = False
    t.right(90 + ang / 2)
    t.backward(radius)
    t.drawmode = drawmode
    t.color = color
    t.speed = speed
    t.heading = heading