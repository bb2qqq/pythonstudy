# coding:utf-8
import sys
import datetime
import pickle
import importlib

pm_user = command = activity_index = None
if len(sys.argv) > 1:
    pm_user = sys.argv[1]
if len(sys.argv) > 2:
    command = sys.argv[2]
if len(sys.argv) > 3:
    if sys.argv[3]:
        activity_index = int(sys.argv[3])


def get_pm(user=''):
    """ Using to generate pm instance """
    try:
        agent = importlib.import_module('%s_pm_cache' % (user))
        current_pm = pickle.loads(agent.__dict__['%s_pm_cache' % (user)])
    except:
        print 'Generate new project manager %s' % user
        current_pm = ProjectManager(user)

    return current_pm


class ProjectManager(object):
    """ raw_dict sample: { 'Activity1': {'create_time': 149222113, 'active_time': 152221313, 'index': 1, progress: 0.0, tips: ['Page 101']}, 'Activity2': {}} """


    def __init__(self, user=''):
        self.raw_dict = {}
        self.user = user
        self.index_dict = {}
        self.__dict__.update({})    # make abbreviation for methods, make the code more readable, preserved for now


    def get_avail_index(self):
        used_index_set = set(self.index_dict.keys())
        avail_index_set = set(range(10000)) - used_index_set
        next_index = sorted(list(avail_index_set))[0]
        return next_index


    def add_activity(self, activity):
        now = datetime.datetime.now()
        index = self.get_avail_index()
        if activity not in self.raw_dict:
            self.raw_dict[activity] = {'create_time': now, 'active_time': now, 'index': index, 'progress': 0.0, 'tips': [ ]}
            self.index_dict[index] = activity

            self.save()

        else:
            print 'The activity is already in your project manager'

    def check_in(self, index):
        now = datetime.datetime.now()
        activity = self.index_dict[index]
        self.raw_dict[activity]['active_time'] = now

    def show_one_activity(self, activity_index):
        activity = self.index_dict[activity_index]
        create_time = str(self.raw_dict[activity]['create_time'])[:19]
        active_time = str(self.raw_dict[activity]['active_time'])[:19]
        tips = self.raw_dict[activity]['tips']
        print activity_index, '\t', activity, '\t', create_time, '\t', active_time
        print 'Tips:'
        for tip in tips:
            print tip


    def show_all_activity(self):
        now = datetime.datetime.now()
        active_limit = datetime.timedelta(days = 3)
        keep_up_limit = datetime.timedelta(days = 10)

        active_list = [activity for activity in self.raw_dict if now - self.raw_dict[activity]['active_time'] <= active_limit ]
        keep_up_list = [activity for activity in self.raw_dict if active_limit < now - self.raw_dict[activity]['active_time'] <= keep_up_limit ]
        frozen_list = [activity for activity in self.raw_dict if now - self.raw_dict[activity]['active_time'] > keep_up_limit ]

        def temp_print(target_list):
            for activity in target_list:
                index = self.raw_dict[activity]['index']
                active_time = str(self.raw_dict[activity]['active_time'])[:19]
                print index, '\t', activity, '\t', active_time

        print '\nActive Project:\n'
        temp_print(active_list)

        print '\nKeeping Up Project:\n'
        temp_print(keep_up_list)

        print '\nFrozen Project:\n'
        temp_print(frozen_list)


    def add_tip(self, activity_index, tip=''):
        activity = self.index_dict[activity_index]
        tip = tip or raw_input().replace('\\n', '\n')
        self.raw_dict[activity]['tips'].append(tip)

        self.save()


    def show_tips(self, activity ):
        for index, tip in enumerate(self.raw_dict['activity']['tip']):
            print index, tip


    def save(self):
        # Please Add something here to avoid mis-saving
        saving_data = pickle.dumps(self)
        f = open('/Users/zen1/zen/pythonstudy/creation/project_manager/%s_pm_cache.py' % self.user , 'w')
        f.write('%s_pm_cache=%r' %  (self.user, saving_data))
        f.close()



if pm_user:
    current_pm = get_pm(user=pm_user)

if command == 'show':
    if activity_index == None:
        current_pm.show_all_activity()
    else:
        current_pm.show_one_activity(activity_index)

elif command == 'check_in':
    current_pm.check_in(activity_index)
    current_pm.show_all_activity()

elif command == 'add_tip':
    current_pm.add_tip(activity_index)
