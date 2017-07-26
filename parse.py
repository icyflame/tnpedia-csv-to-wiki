import csv
file_name = "tnpedia-2016.csv"
output_file = "output-with-subjective.md"
final_text = ""

DEPARTMENT = 0
COURSE = 1
COMPANY = 2
PLACEMENT_DAY = 3
SOURCE_INFO = 5
PACKAGE = 6
POSTING = 7
P1_DESC = 18
P1_QUES = 20

with open(file_name, 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = 1
    header_row = [ ]
    count = 0
    deps_obj = { }
    for row in data:
        if header:
            header = 0
            continue
        dept = row[DEPARTMENT]
        if not dept in deps_obj.keys():
            deps_obj[dept] = [ ]

        deps_obj[dept].append(row)

    print deps_obj

    for department, responses in sorted(deps_obj.iteritems()):
        final_text += "\n***\n## %s" % department

        for response in responses:
            company = response[COMPANY]
            day = response[PLACEMENT_DAY]
            source = response[SOURCE_INFO]
            package = response[PACKAGE]
            posting = response[POSTING]
            p1_desc = response[P1_DESC]
            p1_ques = response[P1_QUES]

            final_text += "\n\n### %s" % company + \
                            "\n\n**%s**" % day + \
                            "\n\n**Source of information:** %s" % source + \
                            "\n\n**Package:** %s" % package + \
                            "\n\n**Posting:** %s" % posting + \
                            "\n\n**Phase 1 Desc:** %s" % p1_desc + \
                            "\n\n**Phase 1 Questions:** %s" % p1_ques

    text_file = open(output_file, "w")
    text_file.write(final_text)
    text_file.close()

    '''

    for row in data:
        if header:
            header_row = row
            header = 0
            continue

        print 'Department: %s' % row[DEPARTMENT]

        template = "%s\n" % row[PLACEMENT_DAY] + \
                    "**Source of information:** %s" % row[SOURCE_INFO]

        final_text += template
        final_text += "\n\n***\n\n"

        count += 1

    print "Read %d responses" % count

    print final_text
    '''
