import latest_earthquake

if __name__ == '__main__':
    print('Main Application')
    result = latest_earthquake.get_data()
    latest_earthquake.print_data(result)
