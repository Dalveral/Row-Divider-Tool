def response(staff_list: list = None) -> None:
    if staff_list:
        print(f'All done. Unique staff: \n {"; ".join(staff_list)}')
    else:
        print('Staff is not found. Please try again.')

    input('Press Enter to exit...')