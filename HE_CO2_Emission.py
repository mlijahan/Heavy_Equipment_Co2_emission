import numpy as np
import psycopg2
import math
import scipy
import scipy.interpolate
import pandas as pd

""" Calculation of Wheel dozers Production, pollutant emission and Cost"""

"""Production and Rimpull of Track type dozers Calculation"""

try:
    connection = psycopg2.connect(database="Earthwork",
                                  user="postgres",
                                  password="Magool@123",
                                  host="localhost",
                                  port="5432")


    class Activity:

        def activity(self):
            self.main_activity_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                       '14', '15',
                                       '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                                       '28',
                                       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                                       '41',
                                       '42', '43']
            self.equipment_package = [['Front End Shovel'], ['Dozer', 'Scraper', 'Backhoe', 'Excavator'],
                                      ['Dozer', 'Excavator'],
                                      ['Dozer'], ['Grader'], ['Dozer', 'Excavator'],
                                      ['Dozer', 'Grader', 'Scraper'],
                                      ['Dozer', 'Scraper'], ['Dozer', 'Loader', 'Scraper', 'Dump Truck'],
                                      ['Grader'],
                                      ['Backhoe', 'Excavator'], ['Loader', 'Backhoe', 'Excavator'],
                                      ['Backhoe', 'Excavator'],
                                      ['Dozer', 'Loader', 'Grader', 'Dump Truck'],
                                      ['Dozer', 'Loader', 'Grader', 'Dump Truck'],
                                      ['Grader'], ['Dozer', 'Grader', 'Dump Truck', 'Backhoe', 'Excavator'],
                                      ['Dozer', 'Grader', 'Dump Truck'], ['Backhoe', 'Excavator'],
                                      ['Dozer', 'Loader'],
                                      ['Scraper'],
                                      ['Dump Truck'], ['Dozer', 'Grader'],
                                      ['Dozer', 'Loader', 'Grader', 'Scraper', 'Dump Truck'],
                                      ['Loader', 'Dump Truck'], ['Excavator'], ['Backhoe'],
                                      ['Dozer', 'Loader', 'Backhoe', 'Excavator'],
                                      ['Backhoe', 'Excavator'], ['Excavator'], ['Backhoe', 'Excavator'],
                                      ['Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Scraper'], ['Dozer', 'Loader'], ['Excavator'],
                                      ['Dozer', 'Grader', 'Dump Truck'],
                                      ['Dozer', 'Scraper', 'Excavator'], ['Dozer', 'Grader', 'Excavator'],
                                      ['Dozer']]

        def select_activit(self):
            self.chosed = input("Please insert activity:\n(1) 'Excavating above grade'\
                \n(2) 'Excavating below grade'\n(3) 'Grubbing'\n(4)'Heavy ripping'\n(5) 'Light ripping'\
                \n(6) 'Tree stump removal'\n(7) 'Topsoil removal/storage'\n(8) 'Rough cutting'\n(9) 'Rough filling'\
                \n(10) 'Finish grading'\n(11) 'Foundation excavation'\n(12) 'Foundation backfilling'\
                \n(13) 'Footing excavation'\n(14) 'Road base construction'\n(15) 'Temporary road'\
                \n(16) 'Haul road maintenance'\n(17) 'Culvert placement'\n(18) 'Earth berm or dam construction'\
                \n(19) 'Drainage ditch maintenance'\n(20) 'Haul less than 500 ft'\n(21) 'Haul 500 ft to 2 miles'\
                \n(22) 'Haul over 2 miles'\n(23) 'Soil windrowing'\n(24) 'Soil spreading'\n(25) 'Excess loose soil removal'\
                \n(26) 'Deep trench excavation'\n(27) 'Shallow trench excavation'\n(28) 'Trench backfilling'\
                \n(29) 'Utility pipe placing — small'\n(30) 'Utility pipe placing — large'\n(31) 'Trench box placement,movement'\
                \n(32) 'trash or debris removal'\n(33) 'Rock removal' \n(34) 'Asphalt paving removal' \n(35) 'Concrete removal'\
                \n(36) 'Structure demo'\n(37) 'Assisting scrapers'\n(38) 'Towing other equipment'\n(39) 'Concrete placement bucket'\
                \n(40) 'Crane pad construction'\n(41) 'Crane pad construction'\n(42) 'Benching'\n(43) 'Side sloping'\n\n")
            self.activity_package = dict(zip(self.main_activity_list, self.equipment_package))
            for k, v in self.activity_package.items():
                if k == self.chosed:
                    print(v)
                    break
            else:
                input("Please insert a new main activity:\n")

        def subactivity(self):
            self.subactivity_volume_unit_machine = []
            n = int(input(
                "Enter ID number of subactivity it's name, paving width , compacted density of asphalt (t/m3):\n\n"))
            for i in range(0, n):
                ele = [input(), int(input()),
                    int(input())]
                self.subactivity_volume_unit_machine.append(ele)
                print(self.subactivity_volume_unit_machine)
            self.subii = [x[1] for x in self.subactivity_volume_unit_machine]
            # if self.subii[0] == 'a':
            #     if self.subii[4] < 100:
            #         F = TrackLoader()
            #         F.TrackLoaders_features()
            #         F.modelnames
            #         F.modelcodes
            #         F.horspower_track
            #         F.horsepowerr_height_temp
            #         F.check_tipping_load
            #         F.required_rimpull
            #         F.compare_Rrimpull_maxtractive_gears
            #         F.realprodactivity_cost()
            #         F.creat_linstext()
            #         F.solution()
            #         F.creat_text()
            #     else:
            #         D = WheelLoader()
            #         D.WheelLoaders_features()
            #         D.modelnames
            #         D.modelcodes
            #         D.horspower_wheel
            #         D.horsepowerr_height_temp
            #         D.check_tipping_load
            #         D.required_rimpull
            #         D.compare_Rrimpull_gears
            #         D.total_cost_per_hour
            #         D.realprodactivity_cost()
            #         D.creat_linstext()
            #         D.solution()
            #         D.creat_text()

        def paving_width(self):
            self.toatal_width = [x[1] for x in self.subactivity_volume_unit_machine]
            return (self.toatal_width)

        def compacted_density_asphalt_tm3(self):
            self.toatal_dens = [x[2] for x in self.subactivity_volume_unit_machine]
            return (self.toatal_dens)

        def hauling_material_type(self):
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT matrial_type FROM weight_material ")
            self.result_surface = self.cur.fetchall()
            print(self.result_surface)
            self.material_type = input("Please select a material type:\n")
            self.cur.execute(f"SELECT * FROM weight_material WHERE matrial_type ={self.material_type}")
            self.result_density = self.cur.fetchall()
            return (self.result_density)

        def surface_type(self):
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT type_surface FROM rolling_resistance ")
            self.result_surface = self.cur.fetchall()
            print(self.result_surface)
            self.surface_type = input("Please select a surface type:\n")
            self.cur.execute(f"SELECT * FROM rolling_resistance WHERE type_surface ={self.surface_type}")
            self.result_rr = self.cur.fetchall()
            return (self.result_rr)

        def fill_factor_wheel_loader(self):
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT material FROM bucket_fill_factor ")
            self.result_fill = self.cur.fetchall()
            print(self.result_fill)
            self.material = input("Please select a material for filling bucket:\n")
            self.min_max_fillfactor = input("Please insert fill factor type:\n(a) 'minimum'\n(b) 'maximum':\n")
            if self.min_max_fillfactor == "a":
                self.cur.execute(f"SELECT wheel_loader_min_percent FROM bucket_fill_factor WHERE material ={self.material}")
                self.result_fills = self.cur.fetchall()
                # print(self.result_fill)
                return (self.result_fill)
            if self.min_max_fillfactor == "b":
                self.cur.execute(f"SELECT wheel_loader_max_percent FROM bucket_fill_factor WHERE material ={self.material}")
                self.result_fills= self.cur.fetchall()
                # print(self.result_fill)
                return (self.result_fills)



        def fill_factor_track_loader(self):
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT Material FROM Bucket_fill_factor ")
            self.result_fill = self.cur.fetchall()
            print(self.result_fill)
            self.material = input("Please select a material for filling bucket:\n")
            self.min_max_fillfactor = input("Please insert fill factor type:\n(a) 'minimum'\n(b) 'maximum':\n")
            if self.min_max_fillfactor == "a":
                self.cur.execute(f"SELECT track_loader_min_percent FROM Bucket_fill_factor WHERE Material ={ self.material}")
                self.result_fill_min = self.cur.fetchall()
                return (self.result_fill_min)
            if self.min_max_fillfactor == "b":
                self.cur.execute(f"SELECT track_loader_max_percent FROM Bucket_fill_factor WHERE Material ={ self.material}")
                self.result_fill_max = self.cur.fetchall()
                return (self.result_fill_max)


    class Asphaltpaver(Activity):
        def asphaletpaver_features(self):
            super().activity()
            super().select_activit()
            super().subactivity()
            self.all_wheelloaders = []
            self.all_wheel_speeds = []
            self.all_wheel_consumption = []
            self.costs_input_wheel = []
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT id, model, emmision_standards FROM cat_asphaltpaver")
            result_models = self.cur.fetchall()
            print(result_models)
            self.model = input("Please select the first paver model ID:\n")
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT id, model , flywheel_power_hp , operating_weight_kg ,\
                                standard_paving_width_mm, turmimg_radius_mm, available_screed FROM cat_asphaltpaver WHERE id ={self.model}")
            self.result = self.cur.fetchall()
            self.all_wheelloaders.append(self.result)
            print(self.all_wheelloaders)
            self.cur.execute(f"SELECT id, model , max_speed_paving_mobiltrac_mmin, max_speed_paving_steeltrack_mmin,\
             max_speed_travel_mobiltrac_kmh, max_speed_travel_steeltrack_kmh, paving_speed_vibratory_mmin, paving_speed_tamperbar_mmin,\
              speed_travel_kmh, paving_speed_mmin, machine_type FROM cat_asphaltpaver WHERE id ={self.model}")
            self.results = self.cur.fetchall()
            self.all_wheel_speeds.append(self.results)
            print(self.all_wheel_speeds)
            self.cur.execute(f"SELECT id, model, capacity_crankcase_galon FROM cat_asphaltpaver WHERE id ={self.model}")
            self.resultss = self.cur.fetchall()
            self.costs_input_wheel.append(self.resultss)
            print(self.costs_input_wheel)
            ques = input("Do you want to select another model?")
            while ques == 'YES':
                self.model = input("Please select another wheel loader model ID:\n")
                self.cur = connection.cursor()
                self.cur.execute(f"SELECT id, model , flywheel_power_hp , operating_weight_kg ,\
                                standard_paving_width_mm, turmimg_radius_mm, available_screed FROM cat_asphaltpaver WHERE id ={self.model}")
                self.result = self.cur.fetchall()
                self.all_wheelloaders.append(self.result)
                print(self.all_wheelloaders)
                self.cur.execute(f"SELECT id, model , max_speed_paving_mobiltrac_mmin, max_speed_paving_steeltrack_mmin,\
             max_speed_travel_mobiltrac_kmh, max_speed_travel_steeltrack_kmh, paving_speed_vibratory_mmin, paving_speed_tamperbar_mmin,\
              speed_travel_kmh, paving_speed_mmin, machine_type FROM cat_asphaltpaver WHERE id ={self.model}")
                self.results = self.cur.fetchall()
                self.all_wheel_speeds.append(self.results)
                print(self.all_wheel_speeds)
                self.cur.execute(f"SELECT id, model, capacity_crankcase_galon FROM cat_asphaltpaver WHERE id ={self.model}")
                self.resultss = self.cur.fetchall()
                self.costs_input_wheel.append(self.resultss)
                print(self.costs_input_wheel)
                ques = input("Do you want to select another model?")
            quess = input("Do you want to estimate cost for each model?")
            if quess == 'YES':
                self.models = [[x[0] for x in self.result] for self.result in self.all_wheelloaders]
                print(self.models)
                self.cost_input_wheelS = []
                for model in self.models:
                    self.cost_input_wheel = []
                    for name in model:
                        self.cost_input_wheel.append(float(input("Please insert price of per gallon of fuel $:\n")))
                        self.cost_input_wheel.append(int(input("Please insert cost of lubricating ($):\n\n")))
                        self.cost_input_wheel.append(int(input("Please operator wage per hour($):\n\n")))
                        self.cost_input_wheel.append(float(input("Please insert total price of tires($):\n")))
                        print(self.cost_input_wheel)
                    self.cost_input_wheelS.append(self.cost_input_wheel)
                    print(self.cost_input_wheelS)

        @property
        def modelnames(self):
            self.modelname = [[x[1] for x in self.result] for self.result in self.all_wheelloaders]
            self.modelnamer = [item for sublist in self.modelname for item in sublist]
            return (self.modelnamer)

        @property
        def modelcodes(self):
            self.modelcoderr = [[x[0] for x in self.result] for self.result in self.all_wheelloaders]
            self.modelcoderN = [item for sublist in self.modelcoderr for item in sublist]
            self.modelcoderS = [str(elem) for elem in self.modelcoderN]
            self.modelcoder = [i + '/' + j for i, j in zip(self.modelcoderS, self.modelnamer)]
            return (self.modelcoder)

        @property
        def horspower(self):
            self.horsepower = [[x[2] for x in self.result] for self.result in self.all_wheelloaders]
            self.horesspower = np.array(self.horsepower)
            self.horsepowerr = [item for sublist in self.horesspower for item in sublist]
            return (self.horsepowerr)

        @property
        def horsepowerr_height_temp(self):
            self.T0 = float(input("Please insert mean of temp of job site in c:\n\n"))
            self.Tc = 288.6
            self.T0_K = 288.6 + self.T0
            self.T0_Tc = self.T0_K / self.Tc
            self.root_T0_Tc = math.sqrt(self.T0_Tc)
            self.p0 = float(input("Please insert mean of height of job site in m:\n\n"))
            self.Pc = 76
            self.pc_p0 = np.round(self.p0 / self.Pc, 2)
            self.tc0 = np.round(1 / self.root_T0_Tc, 2)
            self.real_horsepower = self.horesspower * self.pc_p0 * self.tc0
            self.real_horsepowerr = [item for sublist in self.horesspower for item in sublist]
            return (self.real_horsepowerr)


        @property
        def operating_weight(self):
            self.operating_weights = [[x[3] for x in self.result] for self.result in self.all_wheelloaders]
            self.operating_weights_wheel = np.array(self.operating_weights)
            self.operatingweight_wheelloader = self.operating_weights_wheel * 0.4536
            self.operatingweight_whee = [item for sublist in self.operatingweight_wheelloader for item in sublist]
            self.operatingweight_wheeell = np.array(self.operatingweight_whee)
            return (self.operatingweight_wheeell)

        @property
        def haul_speed(self):
            self.velo = []
            self.tracktype = [[x[10] for x in self.results] for self.results in self.all_wheel_speeds]
            self.tracktypeS = [item for sublist in self.tracktype for item in sublist]
            self.code = [[x[0] for x in self.results] for self.results in self.all_wheel_speeds]
            self.codes = [item for sublist in self.code for item in sublist]
            self.dictmodelv = dict(zip(self.codes, self.tracktypeS))
            for key, value in self.dictmodelv.items():
                if value == 'Tire':
                    self.v1 = [[x[8] for x in self.results if x[0]== key] for self.results in self.all_wheel_speeds]
                    self.vtire = [item for sublist in self.v1 for item in sublist]
                    self.velo.append(self.vtire)

                elif value == 'steel track':
                    self.v2 = [[x[5] for x in self.results if x[0]== key] for self.results in self.all_wheel_speeds]
                    self.vsteel = [item for sublist in self.v2 for item in sublist]
                    self.velo.append(self.vsteel)

                elif value == 'mobile track':
                    self.v3 = [[x[4] for x in self.results if x[0]== key] for self.results in self.all_wheel_speeds]
                    self.vmobile = [item for sublist in self.v3 for item in sublist]
                    self.velo.append(self.vmobile)

            self.velocity = [item for sublist in self.velo for item in sublist]
            self.haulvelocity_mmin = np.array(self.velocity) * 16.67
            return(self.haulvelocity_mmin)

        @property
        def paving_width(self):
            self.compacted_width = [[x[4] for x in self.result] for self.result in self.all_wheelloaders]
            self.compacted_width_array = np.array(self.compacted_width)
            self.compacted_width_inch = self.operating_weights_wheel * 0.03937
            self.compacted_width_in = [item for sublist in self.operatingweight_wheelloader for item in sublist]
            self.compacted_width_inchs = np.array(self.compacted_width_in)
            return (self.compacted_width_inchs)

        @property
        def requierd_lap(self):
            super().activity()
            super().paving_width()
            self.req_lap = np.array(self.toatal_width)/self.paving_width
            self.requ_lap = np.round(self.req_lap + 1)
            return (self.requ_lap)

        @property
        def number_passes(self):
            self.number_band = self.requierd_lap * 2
            self.number_split = self.requierd_lap - 1
            self.laps_splits = self.number_split * 3
            self.total_laps = self.number_band+self.number_split + 2
            return (self.total_laps)

        @property
        def speeds(self, e =0.7):
            self.forward_speed = (self.haul_speed * e) / self.number_passes
            return (self.forward_speed)

        @property
        def real_productivity(self):
            super().activity()
            super().paving_width()
            super().compacted_density_asphalt_tm3()
            self.reals_productivity = (self.speeds*self.toatal_width*self.toatal_dens*60)/1000
            print( self.reals_productivity)
            return(self.reals_productivity)


        @property
        def depreciation_value(self):
            self.delivered_pricexs = []
            self.delivered_pricexs.append([[x[2] for x in self.resultss] for self.resultss in self.costs_input_wheel])
            self.sale_taxs = []
            self.sale_taxs.append([[x[3] for x in self.resultss] for self.resultss in self.costs_input_wheel])
            self.price_tires = []
            self.price_sale_tax = (np.array(self.delivered_pricexs)) * ((np.array(self.sale_taxs)) / 100)
            self.price_after_sale_tax = (np.array(self.delivered_pricexs)) + (self.price_sale_tax)
            self.net_value_depreciation = self.price_after_sale_tax - self.price_sale_tax
            return (self.net_value_depreciation)

        @property
        def depreciation(self, expected_use = 20000):
            self.depreciations = self.depreciation_value / expected_use
            return (self.depreciations)

        @property
        def useful_life(self, expected_use = 20000, expected_use_annually = 1590):
            self.usefull_lifes = expected_use / expected_use_annually
            return (np.round(self.usefull_lifes))

        @property
        def interest_cost(self, expected_use_annually = 1590):
            self.interest_costx = []
            self.interest_costx.append([[x[4] for x in self.resultss] for self.resultss in self.costs_input_wheel])
            self.int_cost = self.useful_life + 1
            self.intt_cost = 2 * self.useful_life
            self.inttt_cost = self.int_cost / self.intt_cost
            self.dep_int_cost = self.depreciation_value * ((np.array(self.interest_costx)) / 100)
            self.dep_int_cosSt = self.dep_int_cost * self.inttt_cost
            self.interest_cosSts = self.dep_int_cosSt / expected_use_annually
            return (np.round(self.interest_cosSts, 2))

        @property
        def insurance_cost(self, expected_use_annually =1590):
            self.insurance_costx = []
            self.insurance_costx.append([[x[5] for x in self.resultss] for self.resultss in self.costs_input_wheel])
            self.ins_cost = self.useful_life + 1
            self.inss_cost = 2 * self.useful_life
            self.insss_cost = self.ins_cost / self.inss_cost
            self.dep_ins_cost = self.depreciation_value * ((np.array(self.insurance_costx)) / 100)
            self.dep_ins_cosSt = self.dep_ins_cost * self.insss_cost
            self.insurance_costs = self.dep_ins_cosSt / expected_use_annually
            return (np.round(self.insurance_costs, 2))

        @property
        def taxes_cost(self, expected_use_annually =1590):
            self.tx_costx = []
            self.tx_costx.append([[x[6] for x in self.resultss] for self.resultss in self.costs_input_wheel])
            self.tx_cost = self.useful_life + 1
            self.txx_cost = 2 * self.useful_life
            self.txxx_cost = self.tx_cost / self.txx_cost
            self.dep_txt_cost = self.depreciation_value * ((np.array(self.tx_costx)) / 100)
            self.dep_txt_cosSt = self.dep_txt_cost * self.txxx_cost
            self.taxes_costs = self.dep_txt_cosSt / expected_use_annually
            return (np.round(self.taxes_costs, 2))

        @property
        def total_hourly_ownership_cost(self):
            self.total_hourly_ownership_costt = self.depreciation + self.interest_cost + self.insurance_cost + self.taxes_cost
            self.total_hourly_ownership_costts = [item for sublist in self.total_hourly_ownership_costt for item in
                                                  sublist]
            self.total_hourly_ownership_costs = [item for sublist in self.total_hourly_ownership_costts for item in
                                                 sublist]
            return (np.round(self.total_hourly_ownership_costs))

        @property
        def year_of_operationn(self):
            self.year_of_operation = []
            self.year_of_operation.append(
                [[int(x[7]) for x in self.resultss] for self.resultss in self.costs_input_wheel])
            return(self.year_of_operation)

        @property
        def yeardigitt(self):
            self.yeardigiit = []
            self.nn = [[int(x[7]) for x in self.resultss] for self.resultss in self.costs_input_wheel]
            for [n] in self.nn:
                self.yeardigiit.append(sum(range(n + 1)))
            self.yeardigit = [[x] for x in self.yeardigiit]
            return (self.yeardigit)

        @property
        def hourly_repair_cost(self, Lifetime_repair_cost_factor=0.6, expected_use_annually = 1590):
            self.Lifetime_repair_cost = Lifetime_repair_cost_factor * self.depreciation_value
            self.year_digits = (np.array(self.year_of_operationn)) / self.yeardigitt
            self.life = self.Lifetime_repair_cost / expected_use_annually
            self.Hourl_yrepair_cost = self.year_digits * self.life
            self.Hourl_yrepair_cost1 = [item for sublist in self.Hourl_yrepair_cost for item in sublist]
            self.Hourl_yrepair_cost2 = [item for sublist in self.Hourl_yrepair_cost1 for item in sublist]
            return (np.round(self.Hourl_yrepair_cost2, 2))

        @property
        def tire_repair_replacement_costs(self):
            self.site_conditions = input("Please insert site condition:\n(a) Zone A: Almost all tires actually wear through the tread due to abrasion.\
                       \n(b) Zone B: Some tires wear out normally while others fail prematurely due to rock cuts, impacts and non-repairable punctures.\
                       \n(c) Zone C: Few, if any, tires wear through the tread because of non-repairable damages, usually from rock cuts, impacts or continuous overloading\n\n ")
            self.price_tires = []
            self.expected_tirelife = []
            for self.cost_input_wheel in self.cost_input_wheelS:
                self.price_tires.append(self.cost_input_wheel[3])

            if self.site_conditions == 'a':
                self.expected_tirelife.append(4500)

            if self.site_conditions == 'b':
                self.expected_tirelife.append(2100)

            if self.site_conditions == 'c':
                self.expected_tirelife.append(750)

            self.tire_repair_replacement_costss = (np.array(self.price_tires)) / np.array(self.expected_tirelife)
            return (np.round(self.tire_repair_replacement_costss, 2))

        @property
        def manual_fuel_consumption_factor(self):
            self.work_condidion = []
            self.work_condidion.append(
                input("Please insert work condition:\n(a) 'Favorable'\n(b) 'Average'\n(c) 'Unfavorable'\n\n "))
            self.max_fuel_consumption_factor = []
            for self.work_condidions in self.work_condidion:
                if self.work_condidions == 'a':
                    self.max_fuel_consumption_factor.append(0.024)

                elif self.work_condidions == 'b':
                    self.max_fuel_consumption_factor.append(0.036)

                else:
                    self.max_fuel_consumption_factor.append(0.047)
                return (np.array(self.max_fuel_consumption_factor))

        @property
        def manual_load_factor(self):
            self.load_factor = []
            self.load_factor.append(
                input("Please insert loader application:\n(a) 'low'\n(b) 'medium'\n(c) 'high'\n\n "))
            self.max_load_factor = []
            for self.load_factors in self.load_factor:
                if self.load_factors == 'a':
                    self.max_load_factor.append(0.25)

                elif self.load_factors == 'b':
                    self.max_load_factor.append(0.5)

                else:
                    self.max_load_factor.append(0.75)
                return (np.array(self.max_load_factor))

        @property
        def manual_fuel_consumption_cost(self):
            self.fuel_cost = []
            for self.cost_input_wheel in self.cost_input_wheelS:
                self.fuel_cost.append(self.cost_input_wheel[0])
            self.manual_fuel_consumption_costs = self.manual_fuel_consumption_factor * self.manual_load_factor * self.fuel_cost * self.real_horsepowerr
            return (self.manual_fuel_consumption_costs)

        @property
        def Lubricating_oil_cost(self):
            self.engin_crankcase = []
            self.engin_crankcase.append([[x[8] for x in self.resultss] for self.resultss in self.costs_input_wheel])
            self.engin_crankcases1 = [item for sublist in self.engin_crankcase for item in sublist]
            self.engin_crankcases2 = [item for sublist in self.engin_crankcases1 for item in sublist]
            self.hours_between_change = []
            self.hours_between_change.append(
                [[x[9] for x in self.resultss] for self.resultss in self.costs_input_wheel])
            self.hours_between_change1 = [item for sublist in self.hours_between_change for item in sublist]
            self.hours_between_change2 = [item for sublist in self.hours_between_change1 for item in sublist]
            self.lubricant_cost = []
            for self.cost_input_wheel in self.cost_input_wheelS:
                self.lubricant_cost.append(self.cost_input_wheel[1])
            self.quantity_of_oil_required = self.real_horsepowerr * np.array(self.max_load_factor)
            self.quantity_of_oil_requiredd = 0.006 * self.quantity_of_oil_required
            self.quantity_of_oil_requireds = self.quantity_of_oil_requiredd / 7.4
            self.que = (np.array(self.engin_crankcases2)) / (np.array(self.hours_between_change2))
            self.Lubricating_Oil_Cost = self.quantity_of_oil_requireds + self.que
            self.Lubricating_Cost = self.Lubricating_Oil_Cost * self.lubricant_cost
            self.lub_cost = np.round(self.Lubricating_Cost, 2)
            return (self.lub_cost)

        @property
        def operating_cost_per_hour(self):
            operating_costs_per_hour = self.hourly_repair_cost + self.tire_repair_replacement_costs + self.manual_fuel_consumption_cost + self.Lubricating_oil_cost
            print(np.round(operating_costs_per_hour, 2))
            return (np.round(operating_costs_per_hour, 2))

        @property
        def operator_wage_per_hour(self):
            self.operator_wage_cost = []
            for self.cost_input_wheel in self.cost_input_wheelS:
                self.operator_wage_cost.append(self.cost_input_wheel[2])
            return (self.operator_wage_cost)

        @property
        def total_cost_per_hour(self):
            self.total_hourly_cost = self.total_hourly_ownership_cost + self.operating_cost_per_hour + self.operator_wage_per_hour
            print(np.round(self.total_hourly_cost, 2))
            return (np.round(self.total_hourly_cost, 2))

        def realprodactivity_cost(self):
            self.realprodactivity_costs = self.real_productivity / self.total_cost_per_hour
            print(self.realprodactivity_costs)
            return (self.realprodactivity_costs)

        def creat_linstext(self):
            super().volume_subactivity()
            self.volumee = self.volume_subactivity()
            print(self.volumee)
            self.volumeestr = '\n'.join([str(elem) for elem in self.volumee])
            print(self.volumeestr)
            self.modelsname = self.modelnamer
            print(self.modelsname)
            self.modelcodess = self.modelcoder
            print(self.modelcodess)
            self.production = np.round(self.reals_productivity)
            print(self.production)
            self.cost = np.round(self.total_hourly_cost)
            print(self.cost)
            self.maxptoc = np.round(self.realprodactivity_costs, 2)
            print(self.maxptoc)

        def solution(self):
            self.dictmodel_maxptoc = dict(zip(self.modelcodess, self.maxptoc))
            for key, value in self.dictmodel_maxptoc.items():
                if value == max(self.maxptoc):
                    self.modelmax = key
                    print(self.modelmax)
            self.dictmodel_pr = dict(zip(self.modelcodess, self.production))
            for key, value in self.dictmodel_pr.items():
                if key == self.modelmax:
                    self.pdmax = value
                    print(self.pdmax)
            self.dictmodel_cost = dict(zip(self.modelcodess, self.cost))
            for key, value in self.dictmodel_cost.items():
                if key == self.modelmax:
                    self.costmax = value
                    print(self.costmax)
            self.dictmodel_maxptoc = dict(zip(self.modelcodess, self.maxptoc))
            for key, value in self.dictmodel_maxptoc.items():
                if value == min(self.maxptoc):
                    self.modelmin = key
                    print(self.modelmin)
            self.dictmodel_pr = dict(zip(self.modelcodess, self.production))
            for key, value in self.dictmodel_pr.items():
                if key == self.modelmin:
                    self.pdmin = value
                    print(self.pdmin)
            self.dictmodel_cost = dict(zip(self.modelcodess, self.cost))
            for key, value in self.dictmodel_cost.items():
                if key == self.modelmin:
                    self.costmin = value
                    print(self.costmin)
            self.indexmodels = [self.modelcodess.index(i) + 1 for i in self.modelcodess]
            self.dictcodemodel_indexmodels = dict(zip(self.modelcodess, self.indexmodels))
            for key, value in self.dictcodemodel_indexmodels.items():
                if key == self.modelmax:
                    self.indexmax = value
                    print(self.indexmax)
            self.dictcodemodel_indexmodels = dict(zip(self.modelcodess, self.indexmodels))
            for key, value in self.dictcodemodel_indexmodels.items():
                if key == self.modelmin:
                    self.indexmin = value
                    print(self.indexmin)
            self.hrmax = np.round(self.volumee / self.pdmax)
            self.listToStrt2 = ' '.join([str(elem) for elem in self.hrmax])
            print(self.listToStrt2)
            self.hrmin = 0

        def creat_text(self):
            nums = str(len(self.modelname))
            print(nums)
            volume = self.volumeestr
            print(volume)
            modelcodemax = self.indexmax
            print(modelcodemax)
            modelcodemin = self.indexmin
            print(modelcodemin)
            nmax = str(self.listToStrt2)
            print(nmax)
            nmin = str(self.hrmin)
            print(nmin)
            pdmax = str(self.pdmax)
            print(pdmax)
            pdmin = str(self.pdmin)
            print(pdmin)
            costmax = str(self.costmax)
            print(costmax)
            costmin = str(self.costmin)
            print(costmin)
            f = ['n:', 'c:']
            g = [nums, volume]
            lines = [f, g]
            lie = ["begin data"]
            w = ["end data"]
            ind = ["index", "nb", "pd", "cost"]
            sol = ["sol:"]
            model = [modelcodemax, modelcodemin]
            numbers = [nmax, nmin]
            prdctons = [pdmax, pdmin]
            costss = [costmax, costmin]
            solu = [model, numbers, prdctons, costss]
            e = self.modelcodess
            b = self.production
            a = self.cost
            c = [e, a, b]

            with open('readnew.txt', 'w') as file:
                for line in zip(*lines):
                    file.write("\n{0} {1}\n".format(*line))
                for x in lie:
                    file.write("\n{0}\n".format(x))
                for x in zip(*c):
                    file.write("{0}\t{1}\t{2}\n".format(*x))
                for x in w:
                    file.write("{0}\n".format(x))
                for x in ind:
                    file.write("\t{0}".format(x))
                for x in sol:
                    file.write("\n{0}\n".format(x))
                for x in zip(*solu):
                    file.write("\t{0}\t{1}\t{2}\t{3}\n".format(*x))

    C = Activity()
    F = Asphaltpaver()
    F.asphaletpaver_features()
    F.modelnames
    F.modelcodes
    F.horspower
    F.horsepowerr_height_temp
    F.operating_weight
    F.haul_speed
    # F.paving_width
    # F.requierd_lap
    # F.number_passes
    # F.speeds
    F.real_productivity
    # F.total_cost_per_hour
    # F.realprodactivity_cost()
    # F.creat_linstext()
    # F.solution()
    # F.creat_text()





    print("Selecting from database succeeded...")
    connection.close()
except:
    connection.rollback()
    print("Selecting from database failed...")
