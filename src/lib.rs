use ewwii_plugin_api::{auto_plugin, PluginInfo};

auto_plugin!(
    DummyStructure,
    PluginInfo::new("com.css.precss", "1.0.0"),
    host,
    {
        host.log("Precss loaded!");
        host.inject_css(include_str!("pre.css"));
    }
);
