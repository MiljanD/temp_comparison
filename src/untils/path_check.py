from pathlib import Path

def check_path():
    current_wd = Path(__file__).parent
    active_chart_path = Path(f"{current_wd.parent}/charts/active/act_chart.png")

    status = False

    if active_chart_path:
        status = True

    return status
