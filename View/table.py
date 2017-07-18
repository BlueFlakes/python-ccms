class Table:
    table = None
    table_sizes = None

    @classmethod
    def table_creator(cls, table_titles, data):
        cls.table = [table_titles] + data
        cls.table_sizes = cls._get_table_sizes()
        table_visualisation = cls._create_table()

        return table_visualisation

    @classmethod
    def _get_table_sizes(cls):
        record_length = len(cls.table[0])
        table_length = len(cls.table)
        empty_space = 3
        temp = []

        for i in range(record_length):
            temp.append([])

            for j in range(table_length):
                temp[i].append(len(cls.table[j][i]))

        max_table_sizes_per_column = [max(column) + (empty_space * 2) for column in temp]

        return max_table_sizes_per_column

    @classmethod
    def _create_table(cls):
        table_visualisation = ''

        for record in cls.table:
            row = cls._make_row(record)
            separator = cls._make_separator(row)
            table_visualisation += separator + '\n' + row + '\n'

        table_visualisation += separator
        table_visualisation = cls._modify_corners(table_visualisation)

        return table_visualisation

    @classmethod
    def _make_row(cls, record):
        row = '|'

        for i, column in enumerate(record):
            max_size_per_column = cls.table_sizes[i]
            bottom_range = int(((max_size_per_column - len(column)) / 2))
            row += (bottom_range * ' ') + column

            if len(column) + (bottom_range * 2) != max_size_per_column:
                bottom_range += 1

            row += (bottom_range * ' ') + '|'

        return row

    @staticmethod
    def _make_separator(row):
        separator = ''

        for i in range(len(row)):
            if i == 0 or i == len(row) - 1:
                separator += '|'

            else:
                if row[i] == '|':
                    separator += '+'

                else:
                    separator += '-'

        return separator

    @staticmethod
    def _modify_corners(table_visualisation):
        table = table_visualisation.split('\n')
        row_length = len(table[0])
        first_separator = '/' + ((row_length - 2) * '-') + '\\'
        last_separator = '\\' + ((row_length - 2) * '-') + '/'

        table[0] = first_separator
        table[-1] = last_separator

        return '\n'.join(table)
