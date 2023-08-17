
""" CO2 Emission Estimator of Heavy Equipment Which Would be implemented in Earthwork Projects"""

import numpy as np
import math

""" Inputs have to insert by the user """
activity = input("Insert the title of the activity:\n\n")
machine_type = int(input("Insert the type of machine:\n(1)Bulldozer \n(2)Wheel Loader "
                     "\n(3)Crawler Loader \n(4)Backhoe Loader \n(5)Backhoe Excavator \n(6)Excavator "
                     "\n(7)FrontShovel"
                     "\n(8)Skid Steer"
                     "\n(9)MotorGrader \n(10)scraper \n(11)Road Roller\n\n"))
manufacturer = input("Insert the manufacturer name of machine:\n\n")
model_name = input("Insert the model name of machine:\n\n")
temperature = int(input("Insert the mean of the temperature in duration of doing activity (C) (-88 to +58) :\n\n"))
altitude = int(input("Insert the mean of the elevation of the job site (m) (0-3000m) :\n\n"))
power = int(input("Insert the power of the bulldozer (hp):\n\n"))
machine_list = []


def machine_name(manufacturer, model_name):
    """ Define the fullname of machine as:
    Manufacturer's name + Tractor's model name + type of blade of bulldozer (S( Straight blade), U( Universal blade), SU(Semi U),...)"""
    manufacturer_case = manufacturer.upper()
    model_case = model_name.upper()
    return f'{manufacturer_case} {model_case}'


def height_air_pressure(altitude):
    """ Define the air pressure (CmhG) of job site in dependence of the height (m) of site above the see """
    height_above_see_m = [0, 300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000]     # possible heights of job site
    airpress_cmhg = [76, 73.3, 70.66, 68.07, 65.58, 63.17, 60.83, 58.6, 56.41, 54.25, 52.2]
    y_new = np.interp(altitude, height_above_see_m, airpress_cmhg)
    return y_new


def site_temperature_effect(temperature):
    """ Define the Temperature of job site in K """
    temp = (273 + temperature) / 288.6    # convert temperature in Celsius to Kelvin
    site_temperature = math.sqrt(temp)
    return site_temperature


def real_power():
    """ Real Horsepower Rating in job site condition
    (Elevation&Temperature of job site make changes in Rated power SAE"""
    power_real = power / ((76/height_air_pressure(altitude)) * site_temperature_effect(temperature))
    return np.round((power_real*0.7457), 2)   # Convert the Power Interval from hp to KW : 1 hp = 0.7457 kw


def machines(machine_type):
    """ Define the type of the machine using the user's input """
    machine_list.append(machine_type)

    for machine in machine_list:
        if machine == 1:
            return bulldozer_co2_emission(co2=10.21, load_factor=0.58)
        elif machine == 2:
            return wheel_loader_co2_emission(co2=10.21, load_factor=0.48)
        elif machine == 3:
            return others_co2_emission(co2=10.21)
        elif machine == 4:
            return backhoe_loader_co2_emission(co2=10.21, load_factor=0.21)
        elif machine == 5:
            return others_co2_emission(co2=10.21)
        elif machine == 6:
            return excavator_co2_emission(co2=10.21, load_factor=0.4)
        elif machine == 7:
            return excavator_co2_emission(co2=10.21, load_factor=0.4)
        elif machine == 8:
            return skid_steer_loader_co2_emission(co2=10.21, load_factor=0.23)
        elif machine == 9:
            return others_co2_emission(co2=10.21)
        elif machine == 10:
            return others_co2_emission(co2=10.21)
        else:
            return road_roller_co2_emission(co2=10.21, load_factor=0.59)


# Functions for CO2 emission calculation of each machine based on load factors and fuel consumption factors
def bulldozer_co2_emission(co2=10.21, load_factor=0.58):
    power_interval = []
    power_interval.append(real_power())
    break_fuel_consumption_rate = []

    for PI in power_interval:   # PI is in KW and break fuel consumption rate is in Kg/KW.hr. --->
        # SOURCE : US EPA, (2010)

        if PI < 18:
            break_fuel_consumption_rate.append(0.271)

        elif 18 < PI < 37:
            break_fuel_consumption_rate.append(0.269)

        elif 37 < PI < 75:
            break_fuel_consumption_rate.append(0.265)

        elif 75 < PI < 130:
            break_fuel_consumption_rate.append(0.260)

        else:
            break_fuel_consumption_rate.append(0.254)

    co2_emission = load_factor * np.array(break_fuel_consumption_rate) * real_power() * co2
    print(
        f'"CO2 emission of {machine_name(manufacturer, model_name)}"'
        f' with diesel fuel "{activity}" is "{np.round(co2_emission[0], 2)}"Kg CO2 per hour')
    return co2_emission


def others_co2_emission(co2=10.21):
    power_interval = []
    power_interval.append(real_power())
    break_fuel_consumption_rate = []
    max_load_factor = []

    for PI in power_interval:  # PI is in KW and break fuel consumption rate is in kgr/KW.hr. --->
        # Mean value, Lindgren (2007)

        if PI < 18:
            break_fuel_consumption_rate.append(0.271)
            max_load_factor.append(0.33)

        elif 18 < PI < 37:
            break_fuel_consumption_rate.append(0.269)
            max_load_factor.append(0.33)

        elif 37 < PI < 75:
            break_fuel_consumption_rate.append(0.265)
            max_load_factor.append(0.33)

        elif 75 < PI < 130:
            break_fuel_consumption_rate.append(0.260)
            max_load_factor.append(0.38)

        else:
            break_fuel_consumption_rate.append(0.254)
            max_load_factor.append(0.34)

    co2_emission = np.array(max_load_factor) * np.array(break_fuel_consumption_rate) * real_power() * co2
    print(
        f'"CO2 emission of {machine_name(manufacturer, model_name)}"'
        f' with diesel fuel "{activity}" is "{np.round(co2_emission[0], 2)}"Kg CO2 per hour')
    return co2_emission


def wheel_loader_co2_emission(co2=10.21, load_factor=0.48):
    power_interval = []
    power_interval.append(real_power())
    break_fuel_consumption_rate = []

    for PI in power_interval:  # PI is in KW and break fuel consumption rate is in kgr/KW.hr. --->
        # SOURCE : US EPA, (2010)

        if PI < 18:
            break_fuel_consumption_rate.append(0.271)

        elif 18 < PI < 37:
            break_fuel_consumption_rate.append(0.269)

        elif 37 < PI < 75:
            break_fuel_consumption_rate.append(0.265)

        elif 75 < PI < 130:
            break_fuel_consumption_rate.append(0.260)

        else:
            break_fuel_consumption_rate.append(0.254)

    co2_emission = load_factor * np.array(break_fuel_consumption_rate) * real_power() * co2
    print(
        f'"CO2 emission of {machine_name(manufacturer, model_name)}"'
        f' with diesel fuel "{activity}" is "{np.round(co2_emission[0], 2)}"Kg CO2 per hour')
    return co2_emission


def backhoe_loader_co2_emission(co2=10.21, load_factor=0.21):
    power_interval = []
    power_interval.append(real_power())
    break_fuel_consumption_rate = []

    for PI in power_interval:  # PI is in KW and break fuel consumption rate is in kgr/KW.hr. --->
        # Persson & Kindblom, (1999)

        if PI < 18:
            break_fuel_consumption_rate.append(0.271)

        elif 18 < PI < 37:
            break_fuel_consumption_rate.append(0.269)

        elif 37 < PI < 75:
            break_fuel_consumption_rate.append(0.265)

        elif 75 < PI < 130:
            break_fuel_consumption_rate.append(0.260)

        else:
            break_fuel_consumption_rate.append(0.254)

    co2_emission = load_factor * np.array(break_fuel_consumption_rate) * real_power() * co2
    print(
        f'"CO2 emission of {machine_name(manufacturer, model_name)}"'
        f' with diesel fuel "{activity}" is "{np.round(co2_emission[0], 2)}"Kg CO2 per hour')
    return co2_emission


def excavator_co2_emission(co2=10.21, load_factor=0.4):
    power_interval = []
    power_interval.append(real_power())
    break_fuel_consumption_rate = []

    for PI in power_interval:  # PI is in KW and break fuel consumption rate is in kgr/KW.hr. --->
        # Persson & Kindblom, (1999)

        if PI < 18:
            break_fuel_consumption_rate.append(0.271)

        elif 18 < PI < 37:
            break_fuel_consumption_rate.append(0.269)

        elif 37 < PI < 75:
            break_fuel_consumption_rate.append(0.265)

        elif 75 < PI < 130:
            break_fuel_consumption_rate.append(0.260)

        else:
            break_fuel_consumption_rate.append(0.254)

    co2_emission = load_factor * np.array(break_fuel_consumption_rate) * real_power() * co2
    print(
        f'"CO2 emission of {machine_name(manufacturer, model_name)}"'
        f' with diesel fuel "{activity}" is "{np.round(co2_emission[0], 2)}"Kg CO2 per hour')
    return co2_emission


def skid_steer_loader_co2_emission(co2=10.21, load_factor=0.23):
    power_interval = []
    power_interval.append(real_power())
    break_fuel_consumption_rate = []

    for PI in power_interval:  # PI is in KW and break fuel consumption rate is in kgr/KW.hr. --->
        # US EPA, (2010)

        if PI < 18:
            break_fuel_consumption_rate.append(0.271)

        elif 18 < PI < 37:
            break_fuel_consumption_rate.append(0.269)

        elif 37 < PI < 75:
            break_fuel_consumption_rate.append(0.265)

        elif 75 < PI < 130:
            break_fuel_consumption_rate.append(0.260)

        else:
            break_fuel_consumption_rate.append(0.254)

    co2_emission = load_factor * np.array(break_fuel_consumption_rate) * real_power() * co2
    print(
        f'"CO2 emission of {machine_name(manufacturer, model_name)}"'
        f' with diesel fuel "{activity}" is "{np.round(co2_emission[0], 2)}"Kg CO2 per hour')
    return co2_emission


def road_roller_co2_emission(co2=10.21, load_factor=0.59):
    power_interval = []
    power_interval.append(real_power())
    break_fuel_consumption_rate = []

    for PI in power_interval:  # PI is in KW and break fuel consumption rate is in kgr/KW.hr. --->
        # US EPA, (2010)

        if PI < 18:
            break_fuel_consumption_rate.append(0.271)

        elif 18 < PI < 37:
            break_fuel_consumption_rate.append(0.269)

        elif 37 < PI < 75:
            break_fuel_consumption_rate.append(0.265)

        elif 75 < PI < 130:
            break_fuel_consumption_rate.append(0.260)

        else:
            break_fuel_consumption_rate.append(0.254)

    co2_emission = load_factor * np.array(break_fuel_consumption_rate) * real_power() * co2
    print(
        f'"CO2 emission of {machine_name(manufacturer, model_name)}"'
        f' with diesel fuel "{activity}" is "{np.round(co2_emission[0], 2)}"Kg CO2 per hour')
    return co2_emission


def main():

    return machines(machine_type)


if __name__ == "__main__":
    main()






