from learning_wavelets.evaluate_tmp.unet_eval import evaluate_unet
from learning_wavelets.training.scripts.unet_training import train_unet

from generic_dask import train_eval_parameter_grid
from results_to_csv import results_to_csv


def evaluate_unet_parameters(
        base_n_filters=None,
        noise_std_train=None,
        n_samples=None,
        exp_id='',
    ):
    if base_n_filters is None:
        base_n_filters = [64]
    if noise_std_train is None:
        noise_std_train = [(0, 55)]
    if n_samples is None:
        n_samples = [None]
    exp_id = f'unet{exp_id}'
    metrics_names, results = train_eval_parameter_grid(
        exp_id,
        train_unet,
        evaluate_unet,
        parameter_grid={
            'base_n_filters': base_n_filters,
            'noise_std_train': noise_std_train,
            'n_samples': n_samples,
        }
    )
    results_df = results_to_csv(
        metrics_names,
        results,
        output_path=f'{exp_id}.csv',
    )
    return results_df