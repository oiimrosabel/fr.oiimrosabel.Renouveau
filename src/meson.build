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
  'main.py',
  'window.py',
  'commands/AptCommands.py',
  'commands/RpmCommands.py',
  'commands/PacmanCommands.py',
  'commands/FlatpakCommands.py',
  'commands/SnapCommands.py',
  'engines/Engine.py',
  'engines/FlatpakEngine.py',
  'engines/OutlookerEngine.py',
  'enums/PackageManager.py',
  'enums/CommandType.py',
  'enums/TerminalStyle.py',
  'enums/UpdateState.py',
  'commands/CommandRepository.py',
  'models/components/FlatpakComponent.py',
  'models/components/OutlookerDialog.py',
  'models/components/SettingsComponent.py',
  'models/components/SnapComponent.py',
  'models/components/SystemComponent.py',
  'models/components/Terminal.py',
  'models/components/UpdateExpanderRow.py',
  'models/components/UpdateRow.py',
  'models/pages/StartPage.py',
  'models/pages/UpdatePage.py',
  'models/pages/FinishPage.py',
  'records/FlatpakRecord.py',
  'records/OutlookerRecord.py',
  'records/SettingsRecord.py',
  'records/SnapRecord.py',
  'records/SystemRecord.py',
]

install_data(updater_sources, install_dir: moduledir)