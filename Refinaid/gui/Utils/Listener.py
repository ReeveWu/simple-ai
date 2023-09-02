# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/02
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.4
'''

from Refinaid.gui.Utils.Update import update_parameters
from Refinaid.gui.Utils.Update import update_plot_x_parameters
from Refinaid.gui.Utils.Update import update_plot_y_parameters
from Refinaid.gui.Utils.Update import update_model_parameters
from Refinaid.gui.Utils.Update import update_preprocessing_data
from Refinaid.gui.Utils.Update import update_training_results

def background_listener(
        dataset_dropdown,
        select_mutiple_parameters_dropdown,
        x_axis_dropdown,
        y_axis_dropdown,
        model_dropdown,
        decision_tree_classifer_title,
        decision_tree_classifer_criterion_dropdown,
        decision_tree_classifer_max_depth_textbox,
        decision_tree_classifer_min_samples_split_slider,
        decision_tree_classifer_min_samples_leaf_slider,
        decision_tree_classifer_max_features_dropdown,
        decision_tree_classifer_max_leaf_nodes_textbox,
        k_neighbors_classifier_title,
        k_neighbors_classifier_slider,
        k_neighbors_classifier_weights_dropdown,
        k_neighbors_classifier_algorithm_dropdown,
        submit_dataset_setting_btn,
        missing_value_checkbox,
        data_scale_dropdown,
        training_slider,
        validation_slider,
        testing_slider,
        preprocessing_data_result,
        train_btn,
        training_results,
        train_img1,
        train_img2,
        train_img3,
        ) -> None:
        dataset_dropdown.change(
            fn=update_parameters,
            inputs=dataset_dropdown,
            outputs=select_mutiple_parameters_dropdown,
        )

        dataset_dropdown.change(
            fn=update_plot_x_parameters,
            inputs=dataset_dropdown,
            outputs=x_axis_dropdown,
        )

        dataset_dropdown.change(
            fn=update_plot_y_parameters,
            inputs=dataset_dropdown,
            outputs=y_axis_dropdown,
        )

        model_dropdown.change(
            fn=update_model_parameters,
            inputs=model_dropdown,
            outputs=[
                decision_tree_classifer_title,
                decision_tree_classifer_criterion_dropdown,
                decision_tree_classifer_max_depth_textbox,
                decision_tree_classifer_min_samples_split_slider,
                decision_tree_classifer_min_samples_leaf_slider,
                decision_tree_classifer_max_features_dropdown,
                decision_tree_classifer_max_leaf_nodes_textbox, 
                k_neighbors_classifier_title,
                k_neighbors_classifier_slider,
                k_neighbors_classifier_weights_dropdown,
                k_neighbors_classifier_algorithm_dropdown,
            ]
        )

        submit_dataset_setting_btn.click(
            fn=update_preprocessing_data, 
            inputs=[
                dataset_dropdown, select_mutiple_parameters_dropdown, 
                missing_value_checkbox, data_scale_dropdown, 
                training_slider, validation_slider, testing_slider], 
            outputs=[preprocessing_data_result]
        )

        train_btn.click(
            fn=update_training_results,
            inputs=[
                preprocessing_data_result,
                model_dropdown,
                decision_tree_classifer_criterion_dropdown,
                decision_tree_classifer_max_depth_textbox,
                decision_tree_classifer_min_samples_split_slider,
                decision_tree_classifer_min_samples_leaf_slider,
                decision_tree_classifer_max_features_dropdown,
                decision_tree_classifer_max_leaf_nodes_textbox,
                k_neighbors_classifier_slider,
                k_neighbors_classifier_weights_dropdown,
                k_neighbors_classifier_algorithm_dropdown,
            ],
            outputs=[
                training_results,
                train_img1,
                train_img2,
                train_img3,
            ],
        )