from monitoring.uss_qualifier.scd.data_interfaces import RequiredUSSCapabilities
from monitoring.monitorlib.locality import Locality
from monitoring.uss_qualifier.scd.simulator.test_definitions.builder import (
    AutomatedTestBuilder,
)


class NominalPlanningTestDefinition(AutomatedTestBuilder):
    def __init__(self, locale: Locality):
        super().__init__(
            name="Nominal Planning Test",
            group="astm-strategic-coordination",
            locale=locale,
        )

    # Temporarily simple copy paste from nominal-planning-1.json
    uss_capabilities: RequiredUSSCapabilities = [
        {
            "capabilities": ["BasicStrategicConflictDetection"],
            "injection_target": {"uss_role": "First-Mover USS"},
            "generate_issue": {
                "test_code": "FirstMoverCapabilities",
                "relevant_requirements": [],
                "severity": "High",
                "subject": "",
                "summary": "Basic strategic conflict detection not supported",
                "details": "USSP indicated it does not support flight authorisation validation, so it cannot perform the First-Mover USS role to test basic strategic conflict detection required by the flight authorisation service in Switzerland.",
            },
        },
        {
            "capabilities": ["BasicStrategicConflictDetection"],
            "injection_target": {"uss_role": "Second USS"},
            "generate_issue": {
                "test_code": "SecondUSSCapabilities",
                "relevant_requirements": [],
                "severity": "High",
                "subject": "",
                "summary": "Basic strategic conflict detection not supported",
                "details": "USSP indicated it does not support flight authorisation validation, so it cannot perform the Second USS role to test basic strategic conflict detection required by the flight authorisation service in Switzerland.",
            },
        },
    ]

    # Temporarily simple copy paste from nominal-planning-1.json
    steps = [
        {
            "name": "Inject flight via First-mover USS",
            "inject_flight": {
                "reference_time": "2023-02-12T10:34:14.483425+00:00",
                "planning_time": "0:05:00",
                "test_injection": {
                    "operational_intent": {
                        "volumes": [
                            {
                                "volume": {
                                    "outline_polygon": {
                                        "vertices": [
                                            {
                                                "lat": 7.477423822749622,
                                                "lng": 46.97491999984008,
                                            },
                                            {
                                                "lat": 7.477423821039847,
                                                "lng": 46.97538499982026,
                                            },
                                            {
                                                "lat": 7.477424770457274,
                                                "lng": 46.97539822817162,
                                            },
                                            {
                                                "lat": 7.477427609667229,
                                                "lng": 46.975411329130466,
                                            },
                                            {
                                                "lat": 7.477432311328011,
                                                "lng": 46.975424176527724,
                                            },
                                            {
                                                "lat": 7.477438830161459,
                                                "lng": 46.97543664663613,
                                            },
                                            {
                                                "lat": 7.477447103388957,
                                                "lng": 46.975448619361856,
                                            },
                                            {
                                                "lat": 7.477457051335981,
                                                "lng": 46.975459979401066,
                                            },
                                            {
                                                "lat": 7.477468578199379,
                                                "lng": 46.97547061735031,
                                            },
                                            {
                                                "lat": 7.477481572969964,
                                                "lng": 46.97548043076024,
                                            },
                                            {
                                                "lat": 7.4774959105015855,
                                                "lng": 46.97548932512221,
                                            },
                                            {
                                                "lat": 7.477511452716338,
                                                "lng": 46.97549721477847,
                                            },
                                            {
                                                "lat": 7.47752804993433,
                                                "lng": 46.97550402374711,
                                            },
                                            {
                                                "lat": 7.477545542315188,
                                                "lng": 46.975509686453854,
                                            },
                                            {
                                                "lat": 7.477563761397435,
                                                "lng": 46.97551414836356,
                                            },
                                            {
                                                "lat": 7.477582531720886,
                                                "lng": 46.9755173665054,
                                            },
                                            {
                                                "lat": 7.477601672516463,
                                                "lng": 46.975519309886806,
                                            },
                                            {
                                                "lat": 7.477620999447144,
                                                "lng": 46.97551995979184,
                                            },
                                            {
                                                "lat": 7.478057000544437,
                                                "lng": 46.97551995980457,
                                            },
                                            {
                                                "lat": 7.478076327475301,
                                                "lng": 46.975519309900726,
                                            },
                                            {
                                                "lat": 7.478095468271412,
                                                "lng": 46.97551736652059,
                                            },
                                            {
                                                "lat": 7.478114238595763,
                                                "lng": 46.97551414838003,
                                            },
                                            {
                                                "lat": 7.478132457679282,
                                                "lng": 46.97550968647161,
                                            },
                                            {
                                                "lat": 7.478149950061773,
                                                "lng": 46.97550402376608,
                                            },
                                            {
                                                "lat": 7.478166547281737,
                                                "lng": 46.97549721479852,
                                            },
                                            {
                                                "lat": 7.4781820894987705,
                                                "lng": 46.97548932514323,
                                            },
                                            {
                                                "lat": 7.478196427032943,
                                                "lng": 46.97548043078203,
                                            },
                                            {
                                                "lat": 7.478209421806301,
                                                "lng": 46.97547061737267,
                                            },
                                            {
                                                "lat": 7.478220948672645,
                                                "lng": 46.975459979423775,
                                            },
                                            {
                                                "lat": 7.478230896622737,
                                                "lng": 46.97544861938469,
                                            },
                                            {
                                                "lat": 7.4782391698533655,
                                                "lng": 46.97543664665883,
                                            },
                                            {
                                                "lat": 7.4782456886899595,
                                                "lng": 46.975424176550064,
                                            },
                                            {
                                                "lat": 7.4782503903538515,
                                                "lng": 46.97541132915219,
                                            },
                                            {
                                                "lat": 7.478253229566841,
                                                "lng": 46.97539822819251,
                                            },
                                            {
                                                "lat": 7.478254178987183,
                                                "lng": 46.975384999840095,
                                            },
                                            {
                                                "lat": 7.478254177277408,
                                                "lng": 46.974919999820244,
                                            },
                                            {
                                                "lat": 7.478253227761765,
                                                "lng": 46.97490677142331,
                                            },
                                            {
                                                "lat": 7.4782503884602685,
                                                "lng": 46.97489367042681,
                                            },
                                            {
                                                "lat": 7.4782456867183855,
                                                "lng": 46.97488082300081,
                                            },
                                            {
                                                "lat": 7.478239167817867,
                                                "lng": 46.974868352873266,
                                            },
                                            {
                                                "lat": 7.478230894540598,
                                                "lng": 46.974856380138455,
                                            },
                                            {
                                                "lat": 7.478220946563947,
                                                "lng": 46.974845020100375,
                                            },
                                            {
                                                "lat": 7.478209419693374,
                                                "lng": 46.974834382162385,
                                            },
                                            {
                                                "lat": 7.47819642493976,
                                                "lng": 46.974824568773556,
                                            },
                                            {
                                                "lat": 7.4781820874502785,
                                                "lng": 46.97481567444202,
                                            },
                                            {
                                                "lat": 7.478166545303149,
                                                "lng": 46.97480778482489,
                                            },
                                            {
                                                "lat": 7.478149948177879,
                                                "lng": 46.9748009759033,
                                            },
                                            {
                                                "lat": 7.4781324559137685,
                                                "lng": 46.97479531325065,
                                            },
                                            {
                                                "lat": 7.478114236970597,
                                                "lng": 46.97479085140123,
                                            },
                                            {
                                                "lat": 7.478095466806278,
                                                "lng": 46.9747876333249,
                                            },
                                            {
                                                "lat": 7.478076326187155,
                                                "lng": 46.97478569001336,
                                            },
                                            {
                                                "lat": 7.478056999447158,
                                                "lng": 46.974785040181715,
                                            },
                                            {
                                                "lat": 7.477621000544429,
                                                "lng": 46.97478504019445,
                                            },
                                            {
                                                "lat": 7.477601673804613,
                                                "lng": 46.974785690027296,
                                            },
                                            {
                                                "lat": 7.477582533186026,
                                                "lng": 46.974787633340085,
                                            },
                                            {
                                                "lat": 7.477563763022608,
                                                "lng": 46.97479085141769,
                                            },
                                        ]
                                    },
                                    "altitude_lower": {
                                        "value": 605.0,
                                        "reference": "W84",
                                        "units": "M",
                                    },
                                    "altitude_upper": {
                                        "value": 635.0,
                                        "reference": "W84",
                                        "units": "M",
                                    },
                                },
                                "time_start": {
                                    "value": "2023-02-12T10:37:14.483425+00:00",
                                    "format": "RFC3339",
                                },
                                "time_end": {
                                    "value": "2023-02-12T10:42:14.483425+00:00",
                                    "format": "RFC3339",
                                },
                            }
                        ],
                        "state": "Accepted",
                        "off_nominal_volumes": [],
                        "priority": 0,
                    },
                    "flight_authorisation": {
                        "uas_serial_number": "1AF49UL5CC5J6K",
                        "operation_category": "Open",
                        "operation_mode": "Vlos",
                        "uas_class": "C0",
                        "identification_technologies": ["ASTMNetRID"],
                        "connectivity_methods": ["cellular"],
                        "endurance_minutes": 30,
                        "emergency_procedure_url": "https://uav.com/emergency",
                        "operator_id": "CHEo5kut30e0mt01-qwe",
                        "uas_id": "",
                        "uas_type_certificate": "",
                    },
                },
                "known_responses": {
                    "acceptable_results": ["Planned"],
                    "incorrect_result_details": {
                        "ConflictWithFlight": {
                            "test_code": "nominal_planning_test",
                            "relevant_requirements": [
                                "An operational intent with no conflicts in space and time should be planned by the USSP."
                            ],
                            "severity": "High",
                            "subject": "Processing of Operational intent data provided should lead to planning of flight",
                            "summary": "The operational intent data provided should have been processed without conflicts",
                            "details": "All operational intent data provided is correct and valid and free of conflict in space and time, therefore it should have been planned by the USSP.",
                        },
                        "Rejected": {
                            "test_code": "nominal_planning_test",
                            "relevant_requirements": [],
                            "severity": "High",
                            "subject": "",
                            "summary": "Injection request for a valid flight was unsuccessful",
                            "details": "All operational intent data provided was complete and correct with no airspace conflicts. The operational intent data should have been processed successfully and flight should have been planned.",
                        },
                        "Failed": {
                            "test_code": "nominal_planning_test",
                            "relevant_requirements": [],
                            "severity": "High",
                            "subject": "",
                            "summary": "Injection request for a valid flight was unsuccessful",
                            "details": "All operational intent data provided was complete and correct with no airspace conflicts. The operational intent data should have been processed successfully and flight should have been planned.",
                        },
                    },
                },
                "injection_target": {"uss_role": "First-Mover USS"},
                "name": "wmejx5p5",
            },
        },
        {
            "name": "Inject flight via Blocked USS",
            "inject_flight": {
                "reference_time": "2023-02-12T10:34:14.483425+00:00",
                "planning_time": "0:05:00",
                "test_injection": {
                    "operational_intent": {
                        "volumes": [
                            {
                                "volume": {
                                    "outline_polygon": {
                                        "vertices": [
                                            {
                                                "lat": 7.474315728091042,
                                                "lng": 46.97716400145211,
                                            },
                                            {
                                                "lat": 7.474303247689658,
                                                "lng": 46.97717412304557,
                                            },
                                            {
                                                "lat": 7.474292276891787,
                                                "lng": 46.9771850331586,
                                            },
                                            {
                                                "lat": 7.474282921352688,
                                                "lng": 46.97719662672131,
                                            },
                                            {
                                                "lat": 7.474275271172041,
                                                "lng": 46.97720879208173,
                                            },
                                            {
                                                "lat": 7.474269400026217,
                                                "lng": 46.97722141208117,
                                            },
                                            {
                                                "lat": 7.4742653644586845,
                                                "lng": 46.977234365182404,
                                            },
                                            {
                                                "lat": 7.474263203335437,
                                                "lng": 46.97724752664021,
                                            },
                                            {
                                                "lat": 7.474262937470636,
                                                "lng": 46.97726076970267,
                                            },
                                            {
                                                "lat": 7.474264569426098,
                                                "lng": 46.97727396683188,
                                            },
                                            {
                                                "lat": 7.47426808348659,
                                                "lng": 46.97728699093222,
                                            },
                                            {
                                                "lat": 7.474273445811106,
                                                "lng": 46.97729971657432,
                                            },
                                            {
                                                "lat": 7.474280604758724,
                                                "lng": 46.97731202120303,
                                            },
                                            {
                                                "lat": 7.4742894913859015,
                                                "lng": 46.97732378631779,
                                            },
                                            {
                                                "lat": 7.47430002011039,
                                                "lng": 46.977334898613684,
                                            },
                                            {
                                                "lat": 7.474312089535409,
                                                "lng": 46.97734525107282,
                                            },
                                            {
                                                "lat": 7.4743255834261335,
                                                "lng": 46.97735474399491,
                                            },
                                            {
                                                "lat": 7.47434037182908,
                                                "lng": 46.977363285957416,
                                            },
                                            {
                                                "lat": 7.474356312323634,
                                                "lng": 46.97737079469613,
                                            },
                                            {
                                                "lat": 7.47437325139364,
                                                "lng": 46.977377197897326,
                                            },
                                            {
                                                "lat": 7.474391025905868,
                                                "lng": 46.97738243389426,
                                            },
                                            {
                                                "lat": 7.474409464681103,
                                                "lng": 46.977386452261086,
                                            },
                                            {
                                                "lat": 7.474428390142731,
                                                "lng": 46.97738921429845,
                                            },
                                            {
                                                "lat": 7.4744476200269405,
                                                "lng": 46.97739069340619,
                                            },
                                            {
                                                "lat": 7.474466969138073,
                                                "lng": 46.97739087533958,
                                            },
                                            {
                                                "lat": 7.474486251132214,
                                                "lng": 46.97738975834647,
                                            },
                                            {
                                                "lat": 7.474505280311834,
                                                "lng": 46.97738735318418,
                                            },
                                            {
                                                "lat": 7.47452387341421,
                                                "lng": 46.97738368301589,
                                            },
                                            {
                                                "lat": 7.474541851376407,
                                                "lng": 46.97737878318756,
                                            },
                                            {
                                                "lat": 7.474559041059788,
                                                "lng": 46.97737270088755,
                                            },
                                            {
                                                "lat": 7.474575276917473,
                                                "lng": 46.9773654946921,
                                            },
                                            {
                                                "lat": 7.474590402588685,
                                                "lng": 46.977357234001225,
                                            },
                                            {
                                                "lat": 7.474604272404609,
                                                "lng": 46.97734799837037,
                                            },
                                            {
                                                "lat": 7.4780602717187445,
                                                "lng": 46.97480899404357,
                                            },
                                            {
                                                "lat": 7.478072750859629,
                                                "lng": 46.97479887202181,
                                            },
                                            {
                                                "lat": 7.47808372039712,
                                                "lng": 46.97478796152745,
                                            },
                                            {
                                                "lat": 7.478093074689058,
                                                "lng": 46.97477636763495,
                                            },
                                            {
                                                "lat": 7.478100723649223,
                                                "lng": 46.97476420200029,
                                            },
                                            {
                                                "lat": 7.478106593614889,
                                                "lng": 46.974751581785505,
                                            },
                                            {
                                                "lat": 7.478110628056212,
                                                "lng": 46.97473862853046,
                                            },
                                            {
                                                "lat": 7.4781127881205816,
                                                "lng": 46.9747254669823,
                                            },
                                            {
                                                "lat": 7.478113053006759,
                                                "lng": 46.97471222389403,
                                            },
                                            {
                                                "lat": 7.478111420165148,
                                                "lng": 46.974699026803876,
                                            },
                                            {
                                                "lat": 7.478107905322289,
                                                "lng": 46.97468600280696,
                                            },
                                            {
                                                "lat": 7.478102542329355,
                                                "lng": 46.974673277331334,
                                            },
                                            {
                                                "lat": 7.478095382836098,
                                                "lng": 46.97466097293006,
                                            },
                                            {
                                                "lat": 7.478086495793389,
                                                "lng": 46.9746492081009,
                                            },
                                            {
                                                "lat": 7.478075966789133,
                                                "lng": 46.97463809614524,
                                            },
                                            {
                                                "lat": 7.47806389722399,
                                                "lng": 46.97462774407688,
                                            },
                                            {
                                                "lat": 7.478050403334804,
                                                "lng": 46.97461825159139,
                                            },
                                            {
                                                "lat": 7.4780356150751714,
                                                "lng": 46.97460971010614,
                                            },
                                            {
                                                "lat": 7.478019674863899,
                                                "lng": 46.97460220187985,
                                            },
                                            {
                                                "lat": 7.478002736213457,
                                                "lng": 46.97459579922035,
                                            },
                                            {
                                                "lat": 7.477984962251586,
                                                "lng": 46.97459056378839,
                                            },
                                            {
                                                "lat": 7.477966524150307,
                                                "lng": 46.974586546003664,
                                            },
                                            {
                                                "lat": 7.477947599477487,
                                                "lng": 46.974583784559336,
                                            },
                                            {
                                                "lat": 7.477928370486799,
                                                "lng": 46.97458230604945,
                                            },
                                            {
                                                "lat": 7.477909022362576,
                                                "lng": 46.974582124712704,
                                            },
                                            {
                                                "lat": 7.4778897414364325,
                                                "lng": 46.97458324229544,
                                            },
                                            {
                                                "lat": 7.47787071339284,
                                                "lng": 46.974585648034825,
                                            },
                                            {
                                                "lat": 7.477852121480946,
                                                "lng": 46.974589318762405,
                                            },
                                            {
                                                "lat": 7.477834144749823,
                                                "lng": 46.974594219127326,
                                            },
                                            {
                                                "lat": 7.47781695632419,
                                                "lng": 46.97460030193667,
                                            },
                                            {
                                                "lat": 7.477800721737151,
                                                "lng": 46.97460750861006,
                                            },
                                            {
                                                "lat": 7.47778559733606,
                                                "lng": 46.974615769743735,
                                            },
                                            {
                                                "lat": 7.477771728776835,
                                                "lng": 46.97462500577891,
                                            },
                                            {
                                                "lat": 7.474315728091042,
                                                "lng": 46.97716400145211,
                                            },
                                        ]
                                    },
                                    "altitude_lower": {
                                        "value": 605.0,
                                        "reference": "W84",
                                        "units": "M",
                                    },
                                    "altitude_upper": {
                                        "value": 635.0,
                                        "reference": "W84",
                                        "units": "M",
                                    },
                                },
                                "time_start": {
                                    "value": "2023-02-12T10:37:14.483425+00:00",
                                    "format": "RFC3339",
                                },
                                "time_end": {
                                    "value": "2023-02-12T10:42:14.483425+00:00",
                                    "format": "RFC3339",
                                },
                            }
                        ],
                        "state": "Accepted",
                        "off_nominal_volumes": [],
                        "priority": 0,
                    },
                    "flight_authorisation": {
                        "uas_serial_number": "1AF49UL5CC5J6K",
                        "operation_category": "Open",
                        "operation_mode": "Vlos",
                        "uas_class": "C0",
                        "identification_technologies": ["ASTMNetRID"],
                        "connectivity_methods": ["cellular"],
                        "endurance_minutes": 30,
                        "emergency_procedure_url": "https://uav.com/emergency",
                        "operator_id": "CHEo5kut30e0mt01-qwe",
                        "uas_id": "",
                        "uas_type_certificate": "",
                    },
                },
                "known_responses": {
                    "acceptable_results": ["ConflictWithFlight"],
                    "incorrect_result_details": {
                        "Rejected": {
                            "test_code": "nominal_planning_test",
                            "relevant_requirements": [],
                            "severity": "High",
                            "subject": "",
                            "summary": "Injection request for a valid flight was unsuccessful",
                            "details": "All operational intent data provided was complete and correct with no airspace conflicts. The operational intent data should have been processed successfully and flight should have been planned.",
                        },
                        "Failed": {
                            "test_code": "nominal_planning_test",
                            "relevant_requirements": [],
                            "severity": "High",
                            "subject": "",
                            "summary": "Injection request for a valid flight was unsuccessful",
                            "details": "All operational intent data provided was complete and correct with no airspace conflicts. The operational intent data should have been processed successfully and flight should have been planned.",
                        },
                        "Planned": {
                            "test_code": "nominal_planning_test",
                            "relevant_requirements": [
                                "A operational intent that has time or space conflict should not be planned by the USS"
                            ],
                            "severity": "High",
                            "subject": "Operational Intent provided should not be sucessfully planned by the USSP",
                            "summary": "The operational intent details provided were generated in such a way that they should not have been planned.",
                            "details": "The co-ordinates of the 4D Operational intent conflicts with an existing operational intent in the area and the processing result should not be a successful planning of the intent.",
                        },
                    },
                },
                "injection_target": {"uss_role": "Second USS"},
                "name": "za0q1nwk",
            },
        },
    ]
