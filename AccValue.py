{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\froman\fcharset0 Times New Roman;}{\f1\fnil\fcharset0 Courier New;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1 
\pard\sb100\sa100\f0\fs24 #Supposed we have 350M to buy a club with existing squad and are interested in club with at least 85 potential ratings, then we should probably go for Tottenham Hotspur, and Aresenal is relatively a bad choice. Their best 11 squad is as follows\par
\par

\pard\f1\fs22 squad_352_adj = ['GK', 'B$', 'B$', 'B$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'W$|T$|M$', 'W$|T$|M$']\par
\par
rating_352_TH_Overall, best_list_352_TH_Overall, value_352_TH_Overall = get_best_squad(squad_352_adj, 'Tottenham Hotspur', 'Overall')\par
rating_352_TH_Potential, best_list_352_TH_Potential, value_352_TH_Potential  = get_best_squad(squad_352_adj, 'Tottenham Hotspur', 'Potential')\par
\par
print('-Overall-')\par
print('Average rating: \{:.1f\}'.format(rating_352_TH_Overall))\par
print('Total Value (M): \{:.1f\}'.format(value_352_TH_Overall))\par
print(best_list_352_TH_Overall)\par
\par
print('-Potential-')\par
print('Average rating: \{:.1f\}'.format(rating_352_TH_Potential))\par
print('Total Value (M): \{:.1f\}'.format(value_352_TH_Potential))\par
print(best_list_352_TH_Potential)\par
}
 