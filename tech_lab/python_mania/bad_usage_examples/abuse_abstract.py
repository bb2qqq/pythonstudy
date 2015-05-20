class TimerTaskMagicSchool(object):
    def __init__(self, config_id, version):
        self.cur_config_id = config_id
        config_version = game_config.contract_reward[config_id].get('version', 0)
        self.sort = game_config.contract_reward.get(self.cur_config_id, {}).get('sort', 0)
        self.config_id = min([k for k, v in game_config.contract_reward.iteritems() if v['sort'] == self.sort and v.get('version', 0) == config_version])
        self.key = 'magic_school_%s' % self.config_id
        self.next_time = 0
        self.tglobal = 0
        self.repeat = 0
        self.version = version
        self.func = lambda x: x


    def is_repeat(self):
        return self.repeat

    def is_global(self):
        return self.tglobal

    def get_key(self):
        return self.key

    def get_func(self):
        return self.func

    def get_next_time(self):
        return self.next_time

    def set_next_time(self, next_time):
        self.next_time = next_time

    # 此处美不胜收，支持*args和 **kwargs, 只为返还给你最真最纯的version
    def get_version(self, *args, **kwargs):
        return self.version

    def set_version(self, version):
        self.version = version

    def get_config_id(self):
        return self.config_id

