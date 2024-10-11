from nicegui import ui, app

import clean_calc

def set_default_input():
    app.storage.user['wage'] = app.storage.user.get('wage', 25.0)
    app.storage.user['number_of_payer'] = app.storage.user.get('number_of_payer', 6.0)
    app.storage.user['amount_per_payer'] =  app.storage.user.get('amount_per_payer', 20.0)
    app.storage.user['cleaning_time_per_visit'] =  app.storage.user.get('cleaning_time_per_visit', 4.0)
    app.storage.user['period'] =  app.storage.user.get('period', 0)


def calc_period():
    money = clean_calc.calucte_money(app.storage.user['number_of_payer'], app.storage.user['amount_per_payer'])
    hours = clean_calc.calculate_hours(money, app.storage.user['wage'])
    no_visits = clean_calc.calculate_number_of_visits(hours, app.storage.user['cleaning_time_per_visit'])
    no_weeks = clean_calc.get_number_of_weeks_per_month_average()
    periode = clean_calc.get_cleaning_period(no_visits, no_weeks)
    
    app.storage.user['periode'] = str(periode)
    
@ui.page('/')
def index():
    set_default_input()
    with ui.grid(columns=1).classes('w-full justify-items-center'):
        with ui.grid(columns=1).classes('gap-2 justify-self-center').style('width: 100%; max-width: 500px;'):
            with ui.card():
                with ui.row().classes('w-full'):
                    ui.number("Wage", on_change=calc_period).bind_value(app.storage.user, 'wage') \
                        .classes('w-full')

                with ui.row().classes('w-full'):
                    ui.number("Number of payer", on_change=calc_period).bind_value(app.storage.user, 'number_of_payer') \
                        .classes('w-full')

                with ui.row().classes('w-full'):
                    ui.number("Amount per payer / €", on_change=calc_period).bind_value(app.storage.user, 'amount_per_payer') \
                        .classes('w-full')
                    ui.slider(min=1, max=50, on_change=calc_period).bind_value(app.storage.user, 'amount_per_payer') \
                        .classes('w-full')
                        
            with ui.card():
                with ui.row().classes('w-full'):
                    ui.number("Time spent on cleaning per visit / h", on_change=calc_period).bind_value(app.storage.user, 'cleaning_time_per_visit') \
                        .classes('w-full')
                    ui.slider(min=1, max=8, on_change=calc_period).bind_value(app.storage.user, 'cleaning_time_per_visit') \
                        .classes('w-full')
                        
            with ui.row().classes('w-full'):
                ui.number(label="Cleaning distance / weeks", format="%.2f").bind_value_from(app.storage.user, 'periode') \
                        .classes('w-full')


ui.run(storage_secret="#+op38923hasfdoDj")        

# def main():
#     set_default_input()
#     # ui.link('/clean_calc', create_ui)
#     ui.run(storage_secret="#+op38923hasfdoDj")
    
# if __name__ in {"__main__",  "__mp_main__"}:
#     main()