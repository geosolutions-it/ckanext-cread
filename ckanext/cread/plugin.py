import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class CREADThemePlugin(plugins.SingletonPlugin):
        '''An example theme plugin.

        '''
        # Declare that this class implements IConfigurer.
        plugins.implements(plugins.IConfigurer)
	plugins.implements(plugins.ITemplateHelpers)

        def update_config(self, config):

                # Add this plugin's templates dir to CKAN's extra_template_paths, so
                # that CKAN will use this plugin's custom templates.
                toolkit.add_template_directory(config, 'templates')

                # Add this plugin's public dir to CKAN's extra_public_paths, so
                # that CKAN will use this plugin's custom static files.
                toolkit.add_public_directory(config, 'public')
				
        def get_helpers(self):
        
       		from ckanext.cread import helpers as cread_helpers
        	return {
                	'build_nav_main_cread': cread_helpers.build_nav_main_cread,
			'_make_menu_item_cread': cread_helpers._make_menu_item_cread,
			'cread_groups_available': cread_helpers.cread_groups_available,
			'get_full_groups_facetslist': cread_helpers.get_full_groups_facetslist
 	      	}
