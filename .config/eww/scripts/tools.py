def color(percentage):
    percentage_diff = 1.0 - (percentage/100)
    red_color = min(255, percentage_diff*2 * 255)
    green_color = min(255, (percentage/100)*2 * 255)
    return '#{:02x}{:02x}{:02x}'.format(int(red_color), int(green_color), 0)