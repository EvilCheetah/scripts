def main():
    pass


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('Terminated...')

    except Exception as e:
        print(e)