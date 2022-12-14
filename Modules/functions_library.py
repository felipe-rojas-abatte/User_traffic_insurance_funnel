from packages_library import *

def Clean_raw_data(df_init):
    ''' Clean raw csv file  '''
    df = df_init.copy()

    # initial number of rows
    n_df_init = len(df)
        
    # checking missing values
    total_n_missing_values = df.isnull().sum().sum()
    if total_n_missing_values == 0:
        print('No missing values on dataset')
    else:
        n_missing_values = df.isnull().sum()
        for i, col in enumerate(n_missing_values.index):
            if n_missing_values[i] != 0:
                print('{} missing values on column: {}'.format(n_missing_values[i], col))
              
    # checking duplicated values
    cut_dup = df.duplicated()
    df_dup = df[cut_dup]
    df_nodup = df[~cut_dup]
    if len(df_dup) != 0:
        print('There are {} duplicated rows'.format(len(df_dup)))
        df_clean = df_nodup
        if len(df_clean) >= len(df):
              print('Warning. No duplicate values were removed')
    else: 
        print("There aren't duplicated rows")
        df_clean = df_nodup
        if len(df_clean) != len(df):
              print('Warning. Duplicate values were removed')

    n_df_end = len(df_clean)
    print('\nNº rows \nbefore cleaning: {}    after cleaning:{} \n'.format(n_df_init, n_df_end))

    return df

def Histogram_plot(ax, df, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats):  
    ''' Compute an 1-D histogram with '''
    ax.set_title(title_name, size=20, color='k')
    plt.xlabel(xaxis_name, fontsize=18)
    plt.ylabel(yaxis_name, fontsize=18)
    plt.xlim(min_bin, max_bin)
    if log_axis:
        plt.yscale('log')

    max_val = df.max()
    min_val = df.min()
    nbins = int((max_val-min_val)/bin_size)  #numero de bins

    y_axis, bins, patches = plt.hist(x=df, bins=nbins, histtype='barstacked', color='royalblue', rwidth=1)
    
    max_y_val = max(y_axis)
    
    main_values = df.describe() 
    media = main_values['mean'] # Mean value
    Q1 = main_values['25%']     # Percentile 25
    Q2 = main_values['50%']     # Percentile 50
    Q3 = main_values['75%']     # Percentile 75
    
    ## Show the descriptive values computed above on the upper right sector of the plot
    if stats:
        if log_axis:
            ax.text(max_val*0.8, max_y_val*1.0, '25%: {:.2f}'.format(Q1), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.6, '50%: {:.2f}'.format(Q2), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.3, '75%: {:.2f}'.format(Q3), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.15, 'X: {:.2f}'.format(media), size=10, color='r')
        else:
            ax.text(max_val*0.8, max_y_val*1.0, '25%: {:.2f}'.format(Q1), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.9, '50%: {:.2f}'.format(Q2), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.8, '75%: {:.2f}'.format(Q3), size=10, color='k')
            ax.text(max_val*0.8, max_y_val*0.7, 'X: {:.2f}'.format(media), size=10, color='r')

    ax.spines['right'].set_color('w')
    ax.spines['top'].set_color('w')


def Barh_plot(ax, df, title_name):
    ''' Horizontal bar plot '''
    categories = df.value_counts().index.tolist()
    values = df.value_counts().tolist()
    values_total = sum(values)
    values_perc = [100*i/values_total for i in values]
    
    ax.set_title(title_name, size=20, color='k')
    
    plt.barh(categories, values_perc, color ='royalblue')
    
    for i, v in enumerate(values_perc):
        ax.text(v+0.2, i, str(round(v, 2))+'%', color='k', va="center")
 
    ax.spines['right'].set_color('w')
    ax.spines['bottom'].set_color('w')
    ax.spines['left'].set_color('w')
    ax.spines['top'].set_color('w')
    ax.tick_params(axis='x', colors='w')
    
def Barh_plot_custom_list(ax, df, title_name, list_of_bars):
    ''' Horizontal bar plot '''
    values = []
    for element in list_of_bars:
        number = df.tolist().count(element)
        values.append(number)  
    values_total = sum(values)
    values_perc = [100*i/values_total for i in values]
    list_of_bars = [str(x) for x in list_of_bars]
    ax.set_title(title_name, size=20, color='k')
    
    plt.barh(list_of_bars, values_perc, color ='royalblue')
    
    for i, v in enumerate(values_perc):
        ax.text(v+0.2, i, str(round(v, 2))+'%', color='k', va="center")
 
    ax.spines['right'].set_color('w')
    ax.spines['bottom'].set_color('w')
    ax.spines['left'].set_color('w')
    ax.spines['top'].set_color('w')
    ax.tick_params(axis='x', colors='w')
    
def Pie_plot(ax, df, title_name, explode, colors):
    ''' Pie plot '''
    categories = df.value_counts().index.tolist()
    values = df.value_counts().tolist()
    
    ax.set_title(title_name, size=20, color='k')
    
    ax.pie(values, explode=explode, labels=categories, autopct='%1.2f%%', shadow=True, startangle=0, colors= colors, textprops={'fontsize': 12})

def Plot_users_data(arg00, arg01, arg02, arg03, arg04, arg05):
    ''' Show a dashboard with all features related to bank client data '''
    fig = plt.figure(figsize=(25,15))
    gs = GridSpec(nrows=2, ncols=3, width_ratios=[1, 1, 1], height_ratios=[1, 1])
    gs.update(wspace = 0.3, hspace = 0.45)

    plt.title('Clients Data', fontsize=30, x=0.5, y=1.06)
   
    all_axes = fig.get_axes()
    for ax in all_axes:
        for sp in ax.spines.values():
            sp.set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])
    
    ########### Age #####################
    df00 = arg00[0]
    bin_size = arg00[1]
    min_bin = arg00[2]
    max_bin = arg00[3]
    title_name = arg00[4]
    xaxis_name = arg00[5]
    yaxis_name = arg00[6]
    log_axis = arg00[7]
    stats = arg00[8]
    
    ax00 = fig.add_subplot(gs[0,0])
    
    Histogram_plot(ax00, df00, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)

    ######### Income #########################
    df01 = arg01[0]
    bin_size = arg01[1]
    min_bin = arg01[2]
    max_bin = arg01[3]
    title_name = arg01[4]
    xaxis_name = arg01[5]
    yaxis_name = arg01[6]
    log_axis = arg01[7]
    stats = arg01[8]
    
    ax01 = fig.add_subplot(gs[0,1])
    
    Histogram_plot(ax01, df01, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)
    
    ######### Premium #########################
    df02 = arg02[0]
    bin_size = arg02[1]
    min_bin = arg02[2]
    max_bin = arg02[3]
    title_name = arg02[4]
    xaxis_name = arg02[5]
    yaxis_name = arg02[6]
    log_axis = arg02[7]
    stats = arg02[8]
    
    ax02 = fig.add_subplot(gs[0,2])
    
    Histogram_plot(ax02, df02, title_name, xaxis_name, yaxis_name, min_bin, max_bin, bin_size, log_axis, stats)
    
    ######### Device #####################
    ax10 = fig.add_subplot(gs[1,0])
    df10 = arg03[0]
    title_name = arg03[1]
    colors = ['royalblue','darkorange','limegreen']
    
    explode = (0, 0, 0)
    Pie_plot(ax10, df10, title_name, explode, colors)
    
    ######### Condition #####################
    ax11 = fig.add_subplot(gs[1,1])
    df11 = arg04[0]
    title_name = arg04[1]
    labels = [0,1,2,3,4,5,6,7]
    
    Barh_plot_custom_list(ax11, df11, title_name, labels)
    
    ######### Top 15 Substitution Brand #####################
    ax12 = fig.add_subplot(gs[1,2])
    df12 = arg05[0]
    title_name = arg05[1]
    labels = ['tv', 'facebook', 'instagram', 'paid_search_nb', 'podcast']
    
    Barh_plot_custom_list(ax12, df12, title_name, labels)
    
    return


def Heatmap_2D(df_init, col1, min1, max1, bin_size1, col2, min2, max2, bin_size2, text_on):
    df = df_init.copy()
    
    cut1 = (df['funnel_steps']=='collect_contact_info')
    cut2 = (df['funnel_steps']=='viewed_quotes')
    cut3 = (df['funnel_steps']=='application_submit')
    cut4 = (df['funnel_steps']=='phone_connect')
    cut5 = (df['funnel_steps']=='sign_and_exam')
    
    fig = plt.figure(figsize=(20,13))
    gs = GridSpec(nrows=3, ncols=3, height_ratios=[1 ,1 ,1.5 ], width_ratios=[1, 1, 0.8])
    gs.update(wspace = 0.3, hspace = 0.35)

    all_axes = fig.get_axes()
    for ax in all_axes:
        for sp in ax.spines.values():
            sp.set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])

    ax1 = fig.add_subplot(gs[0:2,0:2])
    
    plt.title('Heatmap '+col1+'-'+col2+' for final step', fontsize=15)
    plt.xlabel(col1, fontsize=15)
    plt.ylabel(col2, fontsize=15)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(bin_size1))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(bin_size2))
    
    xbin = np.arange(min1, max1, bin_size1) - bin_size1/2
    ybin = np.arange(min2, max2, bin_size2) - bin_size2/2

    hist, xbins, ybins, im = plt.hist2d(df[cut5][col1], df[cut5][col2] , bins=(xbin, ybin), cmap=plt.cm.Blues) 

    if text_on:
        for i in range(len(ybins)-1):
            for j in range(len(xbins)-1):
                ax1.text(xbins[j]+bin_size1/2,ybins[i]+bin_size2/2, '{:.0f}'.format(hist.T[i,j]), color="k", ha="center", va="center", fontweight="bold", fontsize=8)

    ##################################
    ax2 = fig.add_subplot(gs[2,0:2])
    plt.xlabel(col1, fontsize=15)
    plt.ylabel('Nº Clients', fontsize=15)
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(bin_size1))

    n_x, xbins, patches = plt.hist(x=df[col1], bins=xbin, color='g', alpha=0.5, rwidth=0.9, label='started_navigator')
    n_x, xbins, patches = plt.hist(x=df[cut1][col1], bins=xbin, color='r', alpha=1, rwidth=0.9, label='collect_contact_info')
    n_x, xbins, patches = plt.hist(x=df[cut2][col1], bins=xbin, color='m', alpha=1, rwidth=0.9, label='viewed_quotes')
    n_x, xbins, patches = plt.hist(x=df[cut3][col1], bins=xbin, color='y', alpha=1, rwidth=0.9, label='application_submit')
    n_x, xbins, patches = plt.hist(x=df[cut4][col1], bins=xbin, color='orange', alpha=1, rwidth=0.9, label='phone_connect')
    n_x, xbins, patches = plt.hist(x=df[cut5][col1], bins=xbin, color='b', alpha=1, rwidth=0.9, label='sign_and_exam')
    plt.legend(loc='upper right')

    ##################################
    ax3 = fig.add_subplot(gs[0:2,2])
    plt.ylabel(col2, fontsize=15)
    plt.xlabel('Nº Clients', fontsize=15)
    ax3.yaxis.set_major_locator(ticker.MultipleLocator(bin_size2))

    n_y, ybins, patches = plt.hist(x=df[col2], bins=ybin, color='g', alpha=0.5, rwidth=0.9, orientation='horizontal', label='started_navigator')
    n_y, ybins, patches = plt.hist(x=df[cut1][col2], bins=ybin, color='r', alpha=1, rwidth=0.9, orientation='horizontal', label='collect_contact_info')
    n_y, ybins, patches = plt.hist(x=df[cut2][col2], bins=ybin, color='m', alpha=1, rwidth=0.9, orientation='horizontal', label='viewed_quotes')
    n_y, ybins, patches = plt.hist(x=df[cut3][col2], bins=ybin, color='y', alpha=1, rwidth=0.9, orientation='horizontal', label='application_submit')
    n_y, ybins, patches = plt.hist(x=df[cut4][col2], bins=ybin, color='orange', alpha=1, rwidth=0.9, orientation='horizontal', label='phone_connect')
    n_y, ybins, patches = plt.hist(x=df[cut5][col2], bins=ybin, color='b', alpha=1, rwidth=0.9, orientation='horizontal', label='sign_and_exam')
    plt.legend(loc='upper right')

    return

def Heatmap_CR_2D(df_init, col1, min1, max1, bin_size1, ylim, col2, min2, max2, bin_size2, xlim, text_on):
    
    df = df_init.copy()
    
    cut5 = (df['funnel_steps']=='sign_and_exam')
    
    fig = plt.figure(figsize=(20,13))
    gs = GridSpec(nrows=3, ncols=3, height_ratios=[1 ,1 ,1.5 ], width_ratios=[1, 1, 0.8])
    gs.update(wspace = 0.3, hspace = 0.35)

    all_axes = fig.get_axes()
    for ax in all_axes:
        for sp in ax.spines.values():
            sp.set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])

    ax1 = fig.add_subplot(gs[0:2,0:2])
    
    plt.title('Heatmap '+col1+'-'+col2+' for final step', fontsize=15)
    plt.xlabel(col1, fontsize=15)
    plt.ylabel(col2, fontsize=15)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(bin_size1))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(bin_size2))
    
    xbin = np.arange(min1, max1, bin_size1) - bin_size1/2
    ybin = np.arange(min2, max2, bin_size2) - bin_size2/2

    hist, xbins, ybins, im = plt.hist2d(df[cut5][col1], df[cut5][col2] , bins=(xbin, ybin), cmap=plt.cm.Blues) 

    if text_on:
        for i in range(len(ybins)-1):
            for j in range(len(xbins)-1):
                ax1.text(xbins[j]+bin_size1/2,ybins[i]+bin_size2/2, '{:.0f}'.format(hist.T[i,j]), color="k", ha="center", va="center", fontweight="bold", fontsize=8)

    ##################################
    ax2 = fig.add_subplot(gs[2,0:2])
    plt.xlabel(col1, fontsize=15)
    plt.ylabel('Nº Clients', fontsize=15)
    plt.ylim(0,ylim)
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(bin_size1))

    n_x1, xbins1, patches = plt.hist(x=df[col1], bins=xbin, color='w', alpha=0.5, rwidth=0.9, label='Convertion Rate')
    n_x5, xbins5, patches = plt.hist(x=df[cut5][col1], bins=xbin, color='b', alpha=1, rwidth=0.9, label='sign_and_exam')
    
    CR_x = 100*n_x5/n_x1

    for i in range(len(xbins5)-1):
        ax2.text(xbins5[i]+bin_size1/2, n_x5[i]+n_x5[i]*0.2, str(round(CR_x[i], 1))+'%', color="k", ha="center", va="center", rotation=90, fontsize=8) 
    
    plt.legend(loc='upper right')

    ##################################
    ax3 = fig.add_subplot(gs[0:2,2])
    plt.ylabel(col2, fontsize=15)
    plt.xlabel('Nº Clients', fontsize=15)
    plt.xlim(0,xlim)
    ax3.yaxis.set_major_locator(ticker.MultipleLocator(bin_size2))

    n_y1, ybins1, patches = plt.hist(x=df[col2], bins=ybin, color='w', alpha=0.5, rwidth=0.9, orientation='horizontal', label='Convertion Rate')
    n_y5, ybins5, patches = plt.hist(x=df[cut5][col2], bins=ybin, color='b', alpha=1, rwidth=0.9, orientation='horizontal', label='sign_and_exam')
    
    CR_y = 100*n_y5/n_y1
    
    for i in range(len(ybins5)-1):
        ax3.text(n_y5[i]+5, ybins5[i]+bin_size2/2 , str(round(CR_y[i], 1))+'%', color="k", ha="center", va="center", fontsize=8) 
    
    plt.legend(loc='upper right')

    return