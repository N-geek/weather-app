from source import create_app

weather = create_app()

if __name__ == '__main__':
    weather.run(host='0.0.0.0', port=5000, debug = True)