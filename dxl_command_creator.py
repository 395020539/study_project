import json
from configuration_reader import MyConfig


class MyDxlCommand:
    def __init__(self):
        myconfig = MyConfig()
        dic_data = self.read_json_data(myconfig.data_file)
        self.list_dxl_command = self.create_update_dxl(myconfig.doors_project_path, myconfig.new_dic_module, dic_data)

    def create_update_dxl(self, doors_project_path, dic_module, dic_data):
        list_dxl_command_temp = []
        list_dxl_command = []
        print("dic_data len:", len(dic_data))

        dxl_open_module = """
    Module m = edit(DOORS_MODULE, false)
    Object o
    string DATA_NAME = ""
    string DATA_VALUE = ""
                """

        dxl_update_data = """
    for o in all(m) do {
        if (o."Object Text" "" == DATA_NAME){
            o."Wert(e)" = DATA_VALUE
        }
    }
                        """

        dxl_end = """
    save(m)
    close(m)
    return_ "0"
                    """

        for key in dic_data:
            print("key = ", key)
            doors_module = '"{}{}"'.format(doors_project_path, dic_module[key])
            print("doors_module = ", doors_module)

            dxl_declare_module = "const string DOORS_MODULE = {}".format(doors_module)
            print("dxl_declare_module =", dxl_declare_module)

            dxl_declare_data = """
    DATA_NAME = "{}"
    DATA_VALUE = "{}"
                            """.format(key, dic_data[key])

            dxl_update_date_command = dxl_declare_module + dxl_open_module + dxl_declare_data + dxl_update_data + dxl_end
            print("dxl_update_date_command = ", dxl_update_date_command)

            list_dxl_command_temp.append(dxl_update_date_command)
            print("list_dxl_command_temp = ", list_dxl_command_temp)
            print("number of command = ", len(list_dxl_command_temp))

        for dxl_command in list_dxl_command_temp:
            # print(dxl_command)
            # index = list_dxl_command_temp.index(dxl_command)
            # print("index = {}".format(index))
            # print(type(dxl_command))
            new_dxl_command = bytes(dxl_command, encoding='utf-8')
            # print(new_dxl_command)
            # list_dxl_command[index] = new_dxl_command
            list_dxl_command.append(new_dxl_command)
        print("list_dxl_command = \n", list_dxl_command)
        return list_dxl_command

    def read_json_data(self, data_file):
        json_data = ""
        data_json_path = data_file
        try:
            with open(data_json_path, 'r') as f:
                json_data = json.load(f)
                print(f"json_data = \n{json_data}")
        except Exception as e:
            print("An error occurred:", e)
        dic_data = json_data
        print(f"dic_data = \n{dic_data}")

        return dic_data


if __name__ == '__main__':
    dxl_commands = MyDxlCommand()
    print("dxl_commands: ", dxl_commands)

