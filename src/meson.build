blueprints = custom_target('blueprints',
  input: files(
    'shortcuts-dialog.blp',
    'main.blp',
    'pages/start.blp',
    'pages/update.blp',
    'pages/finish.blp',
    'components/flatpak.blp',
    'components/outlooker.blp',
    'components/settings.blp',
    'components/snap.blp',
    'components/system.blp',
    'components/terminal.blp',
    'components/updextrow.blp',
    'components/updrow.blp'
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)


pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'updater'
gnome = import('gnome')

gnome.compile_resources('updater',
  'updater.gresource.xml',
  dependencies: blueprints,
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'updater.in',
  output: 'updater',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x'
)

updater_sources = [
  '__init__.py',


  'commands.py',
  'engines.py',
  'enums.py',
  'main.py',
  'records.py',
  'tools.py',
  'window.py',
  'components/FlatpakComponent.py',
  'components/OutlookerDialog.py',
  'components/SettingsComponent.py',
  'components/SnapComponent.py',
  'components/SystemComponent.py',
  'components/Terminal.py',
  'components/UpdateExpanderRow.py',
  'components/UpdateRow.py',
  'pages/StartPage.py',
  'pages/UpdatePage.py',
  'pages/FinishPage.py',
]

install_data(updater_sources, install_dir: moduledir)