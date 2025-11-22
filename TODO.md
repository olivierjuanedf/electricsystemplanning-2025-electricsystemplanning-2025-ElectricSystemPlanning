TODO
MAIN actions (M)
M0) Unique prod types def. in (i) all data files, (ii) constants of the codes (@dataclass) and (iii) input JSON files 
-> suppressing redundant constants/input data?
M0) Switch to PyPSA 1.0?
M0) Update readme.md with new names for project etc...
M0) Remove unnecessary/redundant constants 
-> align as much as possible on PyPSA language in input data?
MObis) Check marginal cost/efficiency values in elec-europe_params_fixed.json
M1) See "TODO[debug]"
M2) [CR] Voir "TODO[CR]"
M4) Prévoir appui (doc/mini-script ?) pour aider les étudiants à gérer les infaisabilités ? (bcp au début... surtout si on leur fait passer les embûches pédagos - ne pas mettre d'actif défaillance par ex !)
M7) Tester avec des dates start/end sans hh:mm
M8) Sortir/tracer les émissions CO2
M11) Version de Python ok?
M13) Vérif cohérence FuelNames avec ProdTypeNames -> utilité des 2 ?
M14) Virer les gitignore qui traînent...
M16) Tests is_stress_test case...
M19) Ajouter graphe camembert à la DJ -> to show congestion of intercos in an "aggreg. view"
M20) Save output graphs in html to allow interactive discussions
#################### LATER  ################
M5) Trier/simplifier JSON visibles des élèves -> pour que cela soit facile pour eux de rentrer dedans (ne leur laisser voir que les params utilisateurs). Et adapter doc en fonction
M17 (later)) Introduce aggreg. prod types -> "all_res". To avoid typing lists of all RES types for selection...
M18) Reformat data files description with file objects (folder, separators, column names...)
M19) Select only data of considered cys when reading data in dataset.py\get_countries_data (and other filtering...)
-> seems not TB done for all dts

DATA (D)
D0) Unit of hydro data? Scale accordingly when reading
D1) Add ERAA ed. 2024, with climatic modelling...
D2) Pb with hydro data/week idx when both day and week given they seem equal...
D3) Fix solar thermal key issue - identical to the one with solar_pv vs lfsolarpv previously?

DATA ANALYSIS (DA) - before 1st UC run, to get an intuition of the pbs - my_little_europe_data_analysis.py
#################### LATER  ################
DA3) (improve code quality) Avoid creating Dataset object once per data analysis - getting once all data needed (however it should be done
on the product of data needs -> more than needed in general)
DA5) Allow capacity plot/extract - over multiple years and dts?
DA6) Take into account fatal prod (ror) for net demand case
DA7) Replace [-2] by an adaptive index to refer to extra-params idx at some stages
DA8) Allow case (extract, load duration curve) - currently only possible to plot it

TOY EX (T) - my_toy_ex_italy.py
T1) Fullfill long_term_uc/toy_model_params/italy_parameters.py with complem exs in Ita case (hydro, batteries, dsr)
T2) Do NOT mention diff of PV key between capa and CF data -> confusing for the students...
T3) Keep FUEL_SOURCES or too complex for the students?
-> may be redundant with input/long_term_uc/elec-europe_params_fixed.json -> CONFUSING!
T4) Add min/max soc and generation constraints for the stock/hydro
-> needs to do it via Linopy (even for 1.0 version)
In Store object e_min_pu/e_max_pu but some other key params seem to be missing... (recommended in v1.0
doc to use Storage for hydro...)
-> cf. include\dataset_builder.py add_hydro_extreme_levels_constraint and add_hydro_extreme_gen_constraint functions init
T5) Add dyn constraints, and associated params in input (JSON) files
T6) Introduce possibility to parametrize init_soc in input/long_term_uc/elec-europe_params_to-be-modif.json
-> in some extra-params section to be introduced?

EUROPE SIMUS (E) (my_little_europe_lt_uc.py)
E2) Integrate hydraulic storages... with inflows/min SOC data from ERAA
-> min/max levels in PyPSA?
E2bis) ror with p_set input of PyPSA
E3) Usage param auto fulfill interco capa missing -> ??
E4) Add possibility to set Stock (additional to ERAA data) in JSON tb modif input file
#################### LATER  ################
E5) Add possibility to provide additional fatal demand -> for iterations between UC and imperfect disaggreg of an aggregate DSR flex (EV for ex) modeled as a Stock for ex! (cf. OMCEP course)
E6) Reformat/simplify JSON params file (in input/long_term_uc/elec-europe_params_to-be-modif.json
-> suppress "selec" prefix implicit for some params?
E7) Get dual variable associated to link capa constraint
-> not directly provided in PyPSA... needs to get it from Linopy
-> cf. include\dataset_builder.py, get_link_capa_dual_var_opt function init
E8) Connecter qques nouveaux params au JSON Eur -> SOC_init pour les (gros) stocks?
-> Use "from_json_tb_modif" keyword in input\long_term_uc elec-europe_params_fixed.json
(currently only "from_eraa_data" used)

RUNNER (R) (main_runner.py)
R1) Finish v1 runner
-> automatically over multiple projects cloned?
R2) Script to generate some graphs/ppt(s) after launching the runner
-> for archive/discussing live with the students
R3) "Stress tests": blackout on some countries * pts; issue on some intercos; techno. breakthrough on some pts
R4) Save summary of input/output params in a JSON

PLOTS
P1) Eco2mix colors TB completed -> coal; and markets to distinguish agg_prod_type with same colors
P3) Check case with unique curve -> plot_dims obtained from UC ts name (call of def get_dims_from_uc_ts_name)
P4) plot tot export per country (on a unique graph)
-> cf include\dataset_builder.py\init plot_cum_export_flows_at_opt func
P5) Fix pb with plots -> some curves missing (RES) due to plot_params sep ('-' io '_'?)
-> put also an option to add stock contribution (dispatch and store) in this stacked figure
(include\dataset_builder.py\def plot_opt_prod_var)
P6) Set default color in \input\functional_params\plot_params.json if 1 curve only (a group observed that it was - randomly? - 
set to yellow in this case... not very visible!) 

OTHERS
O1) Doc basic use of codespace out of the repot?
O3) / by efficiency in FuelSources and not * for primary cost?
O4) Iberian-peninsula -> Iberia
O7) Check multiple links between two zones possible. Cf. ger-scandinavia AC+DC in CentraleSupélec students hypothesis.
And interco types (hvdc/hvac) ok? Q2Emmanuel NEAU and Jean-Yves BOURMAUD
#################### LATER  ################
O2) Scripts avec qques exemples de base Python ? "[coding tricks]"
O5) Subpart of git with distinguished access-rights between students / TA for docs and data available?
(to avoid conflicts; changes leading to "un-necessary" bugs)
O6) Finish and connect type checker for JSON file values -> using map(func, [val]) and all([true])
-> OK excepting UsageParameters
