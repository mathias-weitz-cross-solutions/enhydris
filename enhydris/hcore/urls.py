from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from enhydris.hcore import views

urlpatterns = patterns(
    '',

    url(r'^$', views.StationListView.as_view(),
        name='station_list'),
    url(r'^stations/l/$', RedirectView.as_view(url='../..')),
    url(r'^stations/d/(?P<pk>\d+)/$', views.StationDetailView.as_view(),
        name='station_detail'),
    url(r'^stations/b/(?P<pk>\d+)/$', views.StationBriefView.as_view(),
        name='station_brief'),
    (r'^stations/edit/(?P<station_id>\d+)/$',
     views.station_edit, {}, 'station_edit'),
    (r'^stations/add/$',
     views.station_add, {}, 'station_add'),
    (r'^stations/delete/(?P<station_id>\d+)/$',
     views.station_delete, {}, 'station_delete'),

    (r'^map/$',
        views.map_view, {}, 'map_view'),

    (r'^embedmap/$',
        views.embedmap_view, {}, 'embedmap_view'),

    (r'^get_subdivision/(?P<division_id>\d+)/$',
     views.get_subdivision, {}, 'get_subdivision'),

    url(r'^instruments/d/(?P<pk>\d+)/$',
        views.InstrumentDetailView.as_view(), name='instrument_detail'),
    (r'^instrument/edit/(?P<instrument_id>\d+)/$',
     views.instrument_edit, {}, 'instrument_edit'),
    (r'^instrument/add/$', views.instrument_add, {}, 'instrument_add'),
    (r'^instrument/delete/(?P<instrument_id>\d+)/$',
     views.instrument_delete, {}, 'instrument_delete'),

    url(r'^timeseries/d/(?P<pk>\d+)/$', views.TimeseriesDetailView.as_view(),
        name='timeseries_detail'),
    (r'^timeseries/data/$',
     views.timeseries_data, {}, 'timeseries_data'),
    (r'^timeseries/d/(?P<object_id>\d+)/download/$',
     views.download_timeseries, {}, 'timeseries_text'),
    (r'^timeseries/d/(?P<object_id>\d+)/bottom/$',
     views.timeseries_bottom, {}, 'timeseries_bottom'),
    (r'^timeseries/edit/(?P<timeseries_id>\d+)/$',
     views.timeseries_edit, {}, 'timeseries_edit'),
    (r'^timeseries/add/$', views.timeseries_add, {}, 'timeseries_add'),
    (r'^timeseries/delete/(?P<timeseries_id>\d+)/$',
     views.timeseries_delete, {}, 'timeseries_delete'),

    (r'^gentityfile/(?P<gf_id>\d+)/download/$',
     views.download_gentityfile, {}, 'gentityfile_dl'),
    (r'^gentityfile/edit/(?P<gentityfile_id>\d+)/$',
     views.gentityfile_edit, {}, 'gentityfile_edit'),
    (r'^gentityfile/add/$', views.gentityfile_add, {}, 'gentityfile_add'),
    (r'^gentityfile/delete/(?P<gentityfile_id>\d+)/$',
     views.gentityfile_delete, {}, 'gentityfile_delete'),

    (r'^gentitygenericdata/(?P<gg_id>\d+)/download/$',
     views.download_gentitygenericdata, {}, 'gentitygenericdata_dl'),
    (r'^gentitygenericdata/edit/(?P<ggenericdata_id>\d+)/$',
     views.gentitygenericdata_edit, {}, 'gentitygenericdata_edit'),
    (r'^gentitygenericdata/add/$', views.gentitygenericdata_add, {},
     'gentitygenericdata_add'),
    (r'^gentitygenericdata/delete/(?P<ggenericdata_id>\d+)/$',
     views.gentitygenericdata_delete, {}, 'gentitygenericdata_delete'),

    (r'^gentityevent/edit/(?P<gentityevent_id>\d+)/$',
     views.gentityevent_edit, {}, 'gentityevent_edit'),
    (r'^gentityevent/add/$', views.gentityevent_add, {},
     'gentityevent_add'),
    (r'^gentityevent/delete/(?P<gentityevent_id>\d+)/$',
     views.gentityevent_delete, {}, 'gentityevent_delete'),

    (r'^gentityaltcode/edit/(?P<gentityaltcode_id>\d+)/$',
     views.gentityaltcode_edit, {}, 'gentityaltcode_edit'),
    (r'^gentityaltcode/add/$', views.gentityaltcode_add, {},
     'gentityaltcode_add'),
    (r'^gentityaltcode/delete/(?P<gentityaltcode_id>\d+)/$',
     views.gentityaltcode_delete, {}, 'gentityaltcode_delete'),

    (r'^overseer/edit/(?P<overseer_id>\d+)/$',
     views.overseer_edit, {}, 'overseer_edit'),
    (r'^overseer/add/$', views.overseer_add, {}, 'overseer_add'),
    (r'^overseer/delete/(?P<overseer_id>\d+)/$',
     views.overseer_delete, {}, 'overseer_delete'),

    (r'^(?P<layer>[^/]+)/kml/$',
     views.kml, {}),

    (r'^bound/$', views.bound, {}),

    url(r'^add/(?P<model_name>.+)/$', views.ModelAddView.as_view(),
        name='model_add'),
)
