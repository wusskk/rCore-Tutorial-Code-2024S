import base

EXPECTED_3 = [
    # ch3_sleep
    r"get_time OK874846493433503412016837396853025022985809856817030594864314238193597287350553565421552812540145171738752270674373716628257762190261267115502211715350164151408034448558033673255260844750863166937171521083578838176447775086862415150446444571391399192386164039374239143566150949185542102664188417755422710719292354145855394270302603667433015911037630435237120920529451653123231969851907395163687120940559952429163442572146241335642! (\d+)",
    "Test sleep OK874846493433503412016837396853025022985809856817030594864314238193597287350553565421552812540145171738752270674373716628257762190261267115502211715350164151408034448558033673255260844750863166937171521083578838176447775086862415150446444571391399192386164039374239143566150949185542102664188417755422710719292354145855394270302603667433015911037630435237120920529451653123231969851907395163687120940559952429163442572146241335642!",

    # ch3_sleep1
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed874846493433503412016837396853025022985809856817030594864314238193597287350553565421552812540145171738752270674373716628257762190261267115502211715350164151408034448558033673255260844750863166937171521083578838176447775086862415150446444571391399192386164039374239143566150949185542102664188417755422710719292354145855394270302603667433015911037630435237120920529451653123231969851907395163687120940559952429163442572146241335642!",

    # ch3_taskinfo
    "string from task info test",
    "Test task info OK874846493433503412016837396853025022985809856817030594864314238193597287350553565421552812540145171738752270674373716628257762190261267115502211715350164151408034448558033673255260844750863166937171521083578838176447775086862415150446444571391399192386164039374239143566150949185542102664188417755422710719292354145855394270302603667433015911037630435237120920529451653123231969851907395163687120940559952429163442572146241335642!",
]

if __name__ == "__main__":
    base.test(EXPECTED_3)