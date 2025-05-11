def specific_volume_liquid(pressure: float):
    # pressure = 4061.224489795918 * x - 4.2142857142857
    # => x = (pressure + 4.2142857142857) / 4061.224489795918
    return (pressure + 4.2142857142857) / 4061.224489795918


def specific_volume_vapor(pressure: float):
    # pressure = -0.331705365626 * x + 10.0011609687797
    # => x = (pressure - 10.0011609687797) / -0.331705365626
    return (pressure - 10.0011609687797) / -0.331705365626
