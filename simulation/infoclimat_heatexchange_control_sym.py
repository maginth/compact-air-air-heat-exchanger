


def control_sym(infoclimat_csv, heat_capacity_hour, confort_temp=24):
	from datetime import datetime
	h = heat_capacity_hour*2
	c = confort_temp
	dt = pd.read_csv(infoclimat_csv, skiprows=4, sep=';')
	x = dt['dh_utc'][1:].to_numpy().astype('datetime64')
	t = x.astype(datetime)
	_t = dt['temperature'][1:].astype(float)
	tM = _t.rolling(h, min_periods=1).max().to_numpy()
	tm = _t.rolling(h, min_periods=1).min().to_numpy()
	ta = _t.rolling(h, min_periods=1).mean().to_numpy()
	t_confort =  np.choose((tM > c) & (tm < c), [np.choose(np.abs(tM - c) > np.abs(tm - c), [tM, tm]), c])
	plt.plot(t, _t, color=(0,1,0,0.3))
	plt.plot(t, tM, color=(1,0,0,0.3))
	plt.plot(t, tm, color=(0,0,1,0.3))
	plt.plot(t, t_confort, color='gold')
	plt.plot(t, ta, color=(1,0,1))
	plt.show()


control_sym('export_infoclimat.csv', 24)