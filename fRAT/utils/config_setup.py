"""Configuration file"""
pages = ['Settings', 'General', 'Analysis', 'Parsing', 'Plotting', 'Scatter_plot',
         'Brain_table', 'Region_barchart', 'Region_histogram']

'''General settings'''
General = {
    'run_steps': {'type': 'OptionMenu', 'Recommended': 'all', 'Options': ['all', 'analyse', 'plot'], 'save_as': 'string',
                  'Description': '"all", "analyse", or "plot". "analyse" to only run analysis steps, "plot" if json files have already been created or "all" to run all steps.',
                  'label': 'Stage(s)'},

    'verbose': {'type': 'CheckButton', 'Recommended': 'true',
                'Description': 'true or false.', 'label': 'Verbose fRAT stages'},

    'verbose_cmd_line_args': {'type': 'CheckButton', 'Recommended': 'false',
                              'Description': 'true or false.', 'label': 'Verbose command line arguments'},

    'multicore_processing': {'type': 'CheckButton', 'Recommended': 'true',
                             'Description': 'true or false. Use multicore processing to use during analysis? Recommended: true'},

    'max_core_usage': {'type': 'OptionMenu', 'Recommended': 'max', 'Options': ['max', 6, 5, 4, 3, 2, 1],  'save_as': 'string',
                       'Description': "'max' to select number of cores available on the system, alternatively an int to manually select number of cores to use. Recommended: 'max'"},

    'brain_file_loc': {'type': 'Entry', 'Recommended': "", 'save_as': 'string',  'label': 'NIFTI/ANALYZE folder location',
                       'Description': 'Either the absolute location of brain files or blank, if blank then a browser window will allow you to search for the files at runtime. If passing in this information as a command line flag, this will be ignored.'},

    'output_folder_loc': {'type': 'Entry', 'Recommended': "", 'save_as': 'string', 'label': 'fRAT output folder location',
                          'Description': 'Either the absolute location of json files or blank, if blank then a browser window will allow you to search for the files at runtime. If passing in this information as a command line flag, this will be ignored.'},

    'file_cleanup': {'type': 'OptionMenu', 'Recommended': 'move', 'Options': ['move', 'delete'],  'save_as': 'string',
                     'Description': 'Move or delete intermediate files.', 'label': 'File cleanup method'},
}

'''Analysis settings'''
Analysis = {
    'atlas_number': {'type': 'OptionMenu', 'Recommended': 'HarvardOxford-cort',  'save_as': 'string', 'label': 'Atlas',
                     'Options': [
                                 'Cerebellum-MNIflirt',
                                 'Cerebellum-MNIfnirt',
                                 'HarvardOxford-cort',
                                 'HarvardOxford-sub',
                                 'JHU-ICBM-labels',
                                 'JHU-ICBM-tracts',
                                 'juelich',
                                 'MNI',
                                 'SMATT-labels',
                                 'STN',
                                 'striatum-structural',
                                 'Talairach-labels',
                                 'Thalamus'
                                 ],
                     'Description': ''},

    'roi_stat_number': {'type': 'OptionMenu', 'Recommended': 'Mean',  'save_as': 'string',  'label': 'ROI statistic',
                        'Options': ['Voxel number', 'Mean', 'Standard Deviation', 'Confidence Interval', 'Minimum value', 'Maximum value'],
                        'Description': 'Set the statistic to scale the brain figures by. Recommended: Mean.'},

    'frac_inten': {'type': 'Scale', 'From': 0, 'To': 1, 'Resolution': 0.05, 'Recommended': 0.4, 'label': 'Fractional intensity',
                   'Description': 'Fractional intensity threshold for BET. Default: 0.4'},

    'dof': {'type': 'Entry', 'Recommended': 12, 'label': 'DOF',
            'Description': 'Degrees of freedom for FLIRT. Recommended: 12'},

    'motion_correct': {'type': 'CheckButton', 'Recommended': 'false',
                       'Description': 'true or false. Note: This will inflate values such as tSNR.'},

    'anat_align': {'type': 'CheckButton', 'Recommended': 'true', 'label': 'Align to anatomical volume',
                   'Description': 'true or false. Recommended: true.'},

    'grey_matter_segment': {'type': 'OptionMenu', 'Recommended': 'fslfast', 'label': 'Grey matter segmentation method',
                            'Options': ['fslfast', 'freesurfer', 'None'], 'save_as': 'string',
                            'Description': '"freesurfer", "fslfast" or "None". \nNote: Requires anatomical align be true to function.'},

    'fslfast_min_prob': {'type': 'Scale', 'Recommended': 0.1, 'From': 0, 'To': 1, 'Resolution': 0.05,
                         'label': 'fslFAST minimum probability', 'Description': 'Recommended: 0.1'},

    'stat_map_folder': {'type': 'Entry', 'Recommended': 'QA_report/', 'save_as': 'string', 'label': 'Statistical map folder',
                        'Description': 'Folder name which contains the statistical map files. Example: QA_report/'},

    'stat_map_suffix': {'type': 'Entry', 'Recommended': '_tSNR.img', 'save_as': 'string', 'label': 'Statistical map suffix',
                        'Description': 'File name suffix of the statistical map files. Include the file extension. Example: _tSNR.img'},

    'bootstrap': {'type': 'CheckButton', 'Recommended': 'false',
                  'Description': 'true or false. Calculate bootstrapped mean and confidence intervals using 10,000 iterations'},

    'conf_level_number': {'type': 'OptionMenu', 'Recommended': '95%, 1.96',
                            'Options': ['80%, 1.28', '85%, 1.44', '90%, 1.64', '95%, 1.96', '98%, 2.33', '99%, 2.58'],
                            'save_as': 'string', 'label': 'Confidence level',
                            'Description': 'Set the confidence level for confidence interval calculations.\n'
                                           'Numbers represent the confidence level and the corresponding critical z value.\n'
                                           'Recommended: 95%, 1.96.'},

    'binary_params': {'type': 'Dynamic', 'Recommended': [''], 'Options': 'Parsing["parameter_dict1"]',
                      'subtype': 'Checkbutton', 'label': 'Binary parameters',
                      'save_as': 'list', 'Description': 'Add parameters here which will either be on or off.'},
}

'''Parsing settings'''
Parsing = {
    'verify_param_method': {'type': 'OptionMenu', 'Recommended': 'table', 'Options': ["table", "name", "manual"], 'save_as': 'string',
                            'label': 'Parameter verification method',
                            'Description': '"table", "name" or "manual". '
                            '\nHow to find parameter values: "table" finds values from spreadsheet document, "name" finds values from file name, "manual" allows you to manually input parameters at runtime.'},

    'parameter_dict1': {'type': 'Entry', 'Recommended': 'MB, SENSE', 'save_as': 'list',  'label': 'Critical parameters',
                        'Description': 'Comma-separated list of parameter names to be parsed for and plotted'},

    'parameter_dict2': {'type': 'Entry', 'Recommended': 'mb, s', 'save_as': 'list', 'label': 'Critical parameter abbreviation',
                        'Description': 'Comma-separated list of terms to parse the file name for. Each entry '
                                       'corresponds to a critical parameter above. \nOptional if using table parameter '
                                       'verification, however if the file name contains this information it can use '
                                       'this information to auto-detect the critical parameters used for each fMRI '
                                       'volume.'},
}

'''General plot settings'''
Plotting = {
    'plot_dpi': {'type': 'Entry', 'Recommended': 200, 'label': 'Figure DPI',
                 'Description': 'Recommended value 600'},

    'plot_font_size': {'type': 'Entry', 'Recommended': 40, 'label': 'Figure font size',
                       'Description': 'Recommended value 30'},

    'plot_scale': {'type': 'Entry', 'Recommended': 10, 'label': 'Figure scale',
                   'Description': 'Recommended value 10'},

    'make_scatter_table': {'type': 'CheckButton', 'Recommended': 'true',  'label': 'Make scatterplots',
                           'Description': 'true or false.'},

    'make_brain_table': {'type': 'CheckButton', 'Recommended': 'true', 'label': 'Make brain visualisations',
                         'Description': 'true or false.'},

    'make_one_region_fig': {'type': 'CheckButton', 'Recommended': 'true', 'label': 'Make regional barcharts',
                            'Description': 'true or false.'},

    'make_histogram': {'type': 'CheckButton', 'Recommended': 'true',  'label': 'Make regional histograms',
                       'Description': 'true or false.'},

    'colorblind_friendly_plot_colours': {'type': 'Entry', 'Recommended': '#ffeda0, #feb24c, #fc4e2a, #bd0026',  'save_as': 'list',
                                         'Description': 'Hex values of colourblind friendly colour scale.'},

    'regional_fig_rois': {'type': 'Entry', 'Recommended': 'Runtime',  'save_as': 'list', 'label': 'ROIs to plot',
                          'Description': "Provide a comma-separated list of regions to plot e.g. [3, 5], the string 'all' for all rois or the string 'Runtime' to provide regions at runtime."},

    'use_same_axis_limits': {'type': 'OptionMenu', 'Recommended': 'Create both', 'Options': ["Same limits", "Different limits", "Create both"],
                          'label': 'Figure axis limits', 'save_as': 'string',
                          'Description': '"Same limits", "Different limits" or "Both". \n'
                                         'Choose whether to create figures with the same x/y limits.'},

}

'''Brain table settings'''
Brain_table = {
    'brain_tight_layout': {'type': 'CheckButton', 'Recommended': 'false',
                'Description': 'true or false. Use a tight layout when laying out the figure. Recommended: false'},

    'brain_fig_value_min': {'type': 'Entry', 'Recommended': 0,
            'Description': 'Provides the minimum value of the colourbar. For example, set minimum to 50 to make areas with values below 50 appear black.\n'
                           'Recommended value: 0'},

    'brain_fig_value_max': {'type': 'Entry', 'Recommended': None,
                            'Description': 'Provides the maximum value of the colourbar. For example, set maximum to 50 to make areas with values above 50 appear as the brighest colour on the colourbar.\n'
                                           'Recommended value: None. Note: will default to 100 for scaled maps.'},

    'brain_fig_file': {'type': 'OptionMenu', 'Recommended': 'Produce all three figures', 'Options': ['Mean', 'Mean (within roi scaled)', 'Mean (mixed roi scaled)', 'Produce all three figures'],
                               'save_as': 'string', 'Description': ''},

    'brain_table_x_size': {'type': 'Entry', 'Recommended': 40,
                            'Description': 'Change the size of the x-axis. Recommended: 40'},

    'brain_table_y_size': {'type': 'Entry', 'Recommended': 10,
                            'Description': 'Change the size of the y-axis. Recommended: 10'},

    'brain_x_coord': {'type': 'Entry', 'Recommended': 91,
                           'Description': 'Voxel location to slice the images at in the x axis. Recommended settings for both variables: 91 or 58'},

    'brain_z_coord': {'type': 'Entry', 'Recommended': 91,
                           'Description': 'Voxel location to slice the images at in the z axis. Recommended settings for both variables: 91 or 58'},

    'brain_table_cols': {'type': 'Dynamic', 'Recommended': 'MB', 'Options': 'Parsing["parameter_dict1"]', 'subtype': 'OptionMenu', 'save_as': 'string',
                         'DefaultNumber': 0, 'Description': ''},

    'brain_table_rows': {'type': 'Dynamic', 'Recommended': 'SENSE', 'Options': 'Parsing["parameter_dict1"]', 'subtype': 'OptionMenu', 'save_as': 'string',
                         'DefaultNumber': 1, 'Description': ''}
}

'''Scatter plot settings'''
Scatter_plot = {

    'table_x_label': {'type': 'Entry', 'Recommended': 'tSNR mean', 'save_as': 'string',
                      'Description': ''},

    'table_y_label': {'type': 'Entry', 'Recommended': 'ROI', 'save_as': 'string',
                      'Description': ''},

    'table_row_order': {'type': 'OptionMenu', 'Recommended': 'both', 'Options': ['roi', 'stat', 'both'], 'save_as': 'string',
                        'Description': 'roi, stat or both. Recommended: both'},

    'table_cols': {'type': 'Dynamic', 'Recommended': 'MB', 'Options': 'Parsing["parameter_dict1"]',
                         'subtype': 'OptionMenu', 'save_as': 'string', 'DefaultNumber': 0,
                         'Description': ''},

    'table_rows': {'type': 'Dynamic', 'Recommended': 'SENSE', 'Options': 'Parsing["parameter_dict1"]',
                         'subtype': 'OptionMenu', 'save_as': 'string', 'DefaultNumber': 1,
                         'Description': ''}
}

'''One region bar chart'''
Region_barchart = {

    'single_roi_fig_label_x': {'type': 'Entry', 'Recommended': 'Multiband factor', 'save_as': 'string',
                               'Description': ""},

    'single_roi_fig_label_y': {'type': 'Entry', 'Recommended': 'temporal Signal to Noise Ratio', 'save_as': 'string',
                               'Description': ""},

    'single_roi_fig_label_fill': {'type': 'Entry', 'Recommended': 'SENSE factor', 'save_as': 'string',
                               'Description': ""},

    'single_roi_fig_x_axis': {'type': 'Dynamic', 'Recommended': 'MB', 'Options': 'Parsing["parameter_dict1"]',
                         'subtype': 'OptionMenu', 'save_as': 'string', 'DefaultNumber': 0,
                         'Description': ''},

    'single_roi_fig_colour': {'type': 'Dynamic', 'Recommended': 'SENSE', 'Options': 'Parsing["parameter_dict1"]',
                         'subtype': 'OptionMenu', 'save_as': 'string', 'DefaultNumber': 1,
                         'Description': ''},

}

'''Region histogram'''
Region_histogram = {

    'histogram_binwidth': {'type': 'Entry', 'Recommended': 5, 'Description': ""},

    'histogram_fig_label_x': {'type': 'Entry', 'Recommended': 'temporal Signal to Noise Ratio', 'save_as': 'string',
                      'Description': ''},

    'histogram_fig_label_y': {'type': 'Entry', 'Recommended': 'Frequency', 'save_as': 'string',
                      'Description': ''},

    'histogram_stat_line_size': {'type': 'Entry', 'Recommended': 1.5,
                                 'Description': ''},

    'histogram_show_mean': {'type': 'CheckButton', 'Recommended': 'true',
                            'Description': 'true or false.'},

    'histogram_show_median': {'type': 'CheckButton', 'Recommended': 'true',
                            'Description': 'true or false.'},

    'histogram_show_legend': {'type': 'CheckButton', 'Recommended': 'true',
                            'Description': 'true or false.'},

    'histogram_fig_x_facet': {'type': 'Dynamic', 'Recommended': 'MB', 'Options': 'Parsing["parameter_dict1"]',
                              'subtype': 'OptionMenu', 'save_as': 'string', 'DefaultNumber': 0,
                              'Description': ''},

    'histogram_fig_y_facet': {'type': 'Dynamic', 'Recommended': 'SENSE',
                              'Options': 'Parsing["parameter_dict1"]',
                              'subtype': 'OptionMenu', 'save_as': 'string',
                              'DefaultNumber': 1, 'Description': ''},

    'histogram_fig_colour': {'type': 'Dynamic', 'Recommended': '#fc4e2a',
                              'Options': 'Plotting["colorblind_friendly_plot_colours"]',
                              'subtype': 'OptionMenu', 'save_as': 'string',
                              'Description': 'Hex value of colour blind friendly colour. Value taken from colorblind friendly plot colours.'}
}
