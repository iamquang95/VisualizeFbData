#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import csv
import operator
import matplotlib
matplotlib.rc('font', family='Arial')
import matplotlib.pyplot as plt

import matplotlib.cm as cmx
import matplotlib.colors as colors

import numpy as np
import unicodedata



class School:

    def __init__(self, id, name, no_students):
        self.id = id
        self.name = name
        self.no_students = no_students

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_no_students(self):
        return self.no_students

def get_cmap(N):
    color_norm  = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv')
    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)
    return map_index_to_rgb_color

class StatisticReport:

    # school [name, number_of_student]

    def __init__(self, schools, no_profiles):
        self.schools = sorted(schools, key=lambda school: school.get_no_students(), reverse=True)
        self.no_profiles = no_profiles

    def get_schools(self):
        return self.schools

    def get_no_profiles(self):
        return self.no_profiles

    def print_bar_chart(self):

        mpl_fig = plt.figure()
        ax = mpl_fig.add_subplot(111)


        no_schools = len(self.schools)
        width = 0.3

        y_pos = np.arange(no_schools)
        names = [x.get_name() for x in self.schools]
        names = [unicode(x, 'utf-8') for x in names]
        # names = [unicodedata.normalize('NFKD', x) for x in names]
        # names = [x.encode('ascii','ignore') for x in names]
        values = [x.get_no_students() for x in self.schools]

        #
        cmap = get_cmap(no_schools + 1)
        colors = [cmap(i) for i in xrange(0, no_schools)]

        for x in xrange(0, 20):
            colors.append(cmap(x))
        plt.barh(y_pos, values, color = colors)
        plt.yticks(y_pos, names)

        # Print number after a chart
        for i, v in enumerate(values):
            percent = float("{0:.2f}".format(v*1.0/self.no_profiles)) * 100

            ax.text(v + 3, i + .25, str(percent)+"%", color='blue', fontweight='bold')

        plt.xlabel("Number of students")
        plt.title("Number of students in top 20 high school ")



        plt.show()

    def print_pie_chart(self):
        mpl_fig = plt.figure()
        ax = mpl_fig.add_subplot(111)
        no_schools = len(self.schools)
        names = [x.get_name() for x in self.schools]
        names = [unicode(x, 'utf-8') for x in names]
        # names = [unicodedata.normalize('NFKD', x) for x in names]
        # names = [x.encode('ascii','ignore') for x in names]
        values = [x.get_no_students() for x in self.schools]

        cmap = get_cmap(no_schools + 1)
        colors = [cmap(i) for i in xrange(0, no_schools)]

        plt.pie(values, labels=names, colors=colors,
            autopct='%1.1f%%', startangle=90)

        plt.show()


def read_school_data(filename):
    schools = []
    with open(filename, 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in reader:
            schools.append(School(row[0], row[1], int(row[2])))
    return schools

def visualize(schools):
    no_profiles = sum([school.get_no_students() for school in schools])
    sr_20_schools = StatisticReport(schools[:20], no_profiles)
    sr_20_schools.print_bar_chart()

    sr_5_schools = StatisticReport(schools[:5], no_profiles)
    sr_5_schools.print_pie_chart()

#read_school_data("high_school_2.csv")
visualize(read_school_data("new_high_school.csv"))
