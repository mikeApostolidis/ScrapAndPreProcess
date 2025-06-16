import inspect

from src.scraper.scraper_module import *
from src.preprocess.preprocess_module import *
import src.settings as settings
from src.db.database import connect_to_db, get_max_date


def main():
    downloadedDir = settings.download_folder_path
    outputDir = settings.final_output_path

    connection = connect_to_db()

    try:
        max_date = get_max_date()
        print("Max Date from Database:", max_date)
    finally:
        connection.close()

    remove_all_files(downloadedDir, settings.zip_folder_path, outputDir)

    try:
        scrap(max_date)
    except Exception as e:
        print(f"An error occurred during scraping: {e}", inspect.currentframe().f_lineno)

    # PANDAS

    convert_excel_to_csv(downloadedDir)

    remove_empty_spaces_before_after_commas(downloadedDir)

    normalize_columns(downloadedDir)
    delete_AA(downloadedDir)
    delete_AA_ROHS(downloadedDir)
    normalize_type(downloadedDir)
    delete_mitronimo(downloadedDir)
    check_and_fix_double_onoma_epwnymo(downloadedDir)

    delete_pinakas(downloadedDir)
    normalize_klados(downloadedDir)
    normalize_klados_values(downloadedDir)
    dieth_ekps(downloadedDir)

    check_moria_pinaka(downloadedDir)
    delete_periferia(downloadedDir)
    add_hmeromhnia(downloadedDir)

    add_orario_values(downloadedDir)
    create_sxoliko_etos(downloadedDir)
    create_sxolia(downloadedDir)

    normalize_perioxi_topothetisis(downloadedDir)
    add_mousika_organa_to_sxolia(downloadedDir)
    remove_empty_spaces_before_after_commas(downloadedDir)
    re_order(downloadedDir)

    normalize_all_columns_names(downloadedDir)

    remove_rows_with_empty_names(downloadedDir)

    merged_path = full_outer_join_csv_files(downloadedDir, outputDir)

    remove_inferior_duplicates(merged_path)

    # END


# In case the csv file is too big and needs to be split into multiple smaller files

    # def split_csv(input_path, output_folder, lines_per_file=18000):
    #     df = pd.read_csv(input_path, encoding='utf-8')
    #     total_rows = len(df)
    #     print(f"Total rows: {total_rows}")
    #
    #     os.makedirs(output_folder, exist_ok=True)
    #
    #     for i in range(0, total_rows, lines_per_file):
    #         chunk = df.iloc[i:i + lines_per_file]
    #         output_filename = os.path.join(output_folder, f"split_part_{i // lines_per_file + 1}.csv")
    #         chunk.to_csv(output_filename, index=False, encoding='utf-8', na_rep='NULL')
    #         print(f"Saved {output_filename}")
    #
    # # Example usage:
    # split_csv(
    #     input_path="C:/sxoli/cleaned_output-2025-06-15-30092.csv",
    #     output_folder="C:/sxoli/split_output",
    #     lines_per_file=13000
    # )


if __name__ == "__main__":
    main()
