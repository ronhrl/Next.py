def read_file(file_name):
    try:
        f = open(file_name)
        f.read()
        return "__CONTENT_START__\n" + f.read() + "\n" + "__CONTENT_END__\n"

    except:
        return "__CONTENT_START__\n" + "__NO_SUCH_FILE\n" + "__CONTENT_END__\n"
    finally:
        f.close()
