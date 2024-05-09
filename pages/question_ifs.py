import streamlit as st
import requests
from groq import Groq  # Adjust the import statement here

# Placeholder for the long text (replace with actual content)
long_text_placeholder = """
1 Governance and commitment
1.1 Policy
1.1.1* The senior management shall develop, implement and maintain a corporate policy, which shall
include, at a minimum:
• food safety, product quality, legality and authenticity
• customer focus
• food safety culture
• sustainability.
This corporate policy shall be communicated to all employees and shall be broken down into
specific objectives for the relevant departments.
Objectives about food safety culture shall include, at a minimum, communication about food safety
policies and responsibilities, training, employee feedback on food safety related issues and performance measurement.
1.1.2 All relevant information related to food safety, product quality, legality and authenticity shall be
communicated effectively and in a timely manner to the relevant personnel.
1.2 Corporate structure
1.2.1* KO N° 1: The senior management shall ensure that employees are aware of their responsibilities
related to food safety and product quality and that mechanisms are implemented to monitor
the effectiveness of their operation. Such mechanisms shall be identified and documented.
1.2.2 The senior management shall provide sufficient and appropriate resources to meet the product
and process requirements.
1.2.3* The department responsible for food safety and quality management shall have a direct reporting
relationship to the senior management. An organisational chart, showing the structure of the
company, shall be documented and maintained.
1.2.4 The senior management shall ensure that all processes (documented and undocumented) are
known by the relevant personnel and are applied consistently
1.2.5* The senior management shall maintain a system to ensure that the company is kept informed of
all relevant legislation, scientific and technical developments, industry codes of practice, food
safety and product quality issues, and that they are aware of factors that can influence food defence
and food fraud risks.
1.2.6* The senior management shall ensure that the certification body is informed of any changes that
may affect the company’s ability to conform to the certification requirements. This shall include,
at a minimum:
• any legal entity name change
• any production site location change.
For the following specific situations:
• any product recall
• any product recall and/or withdrawal decided by authorities for food safety and/or food fraud
reasons
• any visit from authorities which results in mandatory action connected to food safety, and/or
food fraud
the certification body shall be informed within three (3) working days.
1.3 Management review
1.3.1* The senior management shall ensure that the food safety and quality management system is
reviewed. This activity shall be planned within a 12-month period and its execution shall not exceed
15 months. Such reviews shall include, at a minimum:
• a review of objectives and policies including elements of food safety culture
• results of audits and site inspections
• positive and negative customer feedback
• process compliance
• food fraud assessment outcome
• food defence assessment outcome
• compliance issues
• status of corrections and corrective actions
• notifications from authorities.
1.3.2 Actions from the management review shall be aimed at supporting improvement. The management
review shall assess follow-up actions from previous management reviews and any change that
could affect the food safety and quality management system. The management review shall be
fully documented.
1.3.3 The senior management shall identify and review (e.g. by internal audits or on-site inspections)
the infrastructure and work environment needed to ensure food safety, product quality, legality
and authenticity, at least once within a 12-month period, or whenever significant changes occur.
This shall include, at a minimum:
• buildings
• supply systems
• machines and equipment
• transport
• staff facilities
• environmental conditions
• hygienic conditions
• workplace design
• external influences (e.g. noise, vibration).
Based on risks, the results of the review shall be considered for investment planning.
 Food safety and quality management system
2.1 Quality management
2.1.1 Document management
2.1.1.1 A procedure shall be documented, implemented and maintained to control documents and their
amendments. All documents which are necessary for compliance with food safety, product quality,
legality, authenticity and customer requirements shall be available in their latest version. The reason
for any amendments to documents, critical to those requirements, shall be recorded.
2.1.1.2 The food safety and quality management system shall be documented, implemented and maintained
and shall be kept in one secure location. This applies to both physical and/or digital documented
systems.
2.1.1.3* All documents shall be legible, unambiguous and comprehensive. They shall be available to the
relevant personnel at all times.
2.1.2 Records and documented information
2.1.2.1 Records and documented information shall be legible, properly completed and genuine. They shall
be maintained in a way that subsequent revision or amendment is prohibited. If records are documented electronically, a system shall be maintained to ensure that only authorised personnel
have access to create or amend those records (e.g. password protection).
2.1.2.2* All records and documented information shall be kept in accordance with legal and customer
requirements. If no such requirements are defined, records and documented information shall be
kept for a minimum of one year after the shelf life. For products which have no shelf life, the duration
of record and documented information keeping shall be justified and this justification shall be
documented.
2.1.2.3 Records and documented information shall be securely stored and easily accessible.
2.2 Food safety management
2.2.1 HACCP plan
2.2.1.1* The basis of the company’s food safety management system shall be a fully implemented, systematic
and comprehensive HACCP based plan, following the Codex Alimentarius principles, good manufacturing practices, good hygiene practices and any legal requirements of the production and
destination countries which may go beyond such principles. The HACCP plan shall be specific and
implemented at the production site.
2.2.1.2* The HACCP plan shall cover all raw materials, packaging materials, products or product groups, as
well as every process from incoming goods up to the dispatch of finished products, including
product development.
2.2.1.3 The HACCP plan shall be based upon scientific literature or expert advice obtained from other
sources, which may include: trade and industry associations, independent experts and authorities.
This information shall be maintained in line with any new technical process development.
2.2.1.4 In the event of changes to raw materials, packaging materials, processing methods, infrastructure
and/or equipment, the HACCP plan shall be reviewed to ensure that product safety requirements
are complied with.
2.3 HACCP analysis
2.3.1 HACCP team
2.3.1.1 Assemble HACCP team:
The HACCP team shall have the appropriate specific knowledge and expertise and be a multidisciplinary team which includes operational staff.
2.3.1.2 Those responsible for the development and maintenance of the HACCP plan shall have an internal
team leader and shall have received appropriate training in the application of the HACCP principles
and specific knowledge of the products and processes.
2.3.2 Product description
2.3.2.1 A full description of the product shall be documented and maintained and shall contain all relevant
information on product safety, which includes, at a minimum:
• composition
• physical, organoleptic, chemical and microbiological characteristics
• legal requirements for the food safety of the product
• methods of treatment, packaging, durability (shelf life)
• conditions for storage, method of transport and distribution.
2.3.3 Identify intended use and users of the product
2.3.3.1 The intended use of the product shall be described in relation to the expected use of the product
by the end consumer, taking vulnerable groups of consumers into account.
2.3.4 Construct flow diagram
2.3.4.1 A flow diagram shall be documented and maintained for each product, or product group, and for
all variations of the processes and sub-processes (including rework and reprocessing). The flow
diagram shall identify every step and each control measure defined for CCPs and other control
measures. It shall be dated, and in the event of any change, shall be updated.
2.3.5 On-site confirmation of the flow diagram
2.3.5.1 Representatives of the HACCP team shall verify the flow diagram through on-site verifications, at
all operation stages and shifts. Where appropriate, amendments to the diagram shall be made.
2.3.6 Conduct a hazard analysis for each step
2.3.6.1 A hazard analysis shall be conducted for all possible and expected physical, chemical (including
radiological and allergens) and biological hazards. The analysis shall also include hazards linked to
materials in contact with food, packaging materials as well as hazards related to the work environment. The hazard analysis shall consider the likely occurrence of hazards and the severity of their
adverse health effects. Consideration shall be given to the specific control measures that shall be
applied to control each significant hazard.
2.3.7 Determining critical control points and other control measures
2.3.7.1 Determining whether the step at which a control measure is applied is a CCP in the HACCP system
shall be facilitated by using a decision tree or other tool(s), which demonstrates a logical reasoned
approach.
2.3.8 Establish validated critical limits for each CCP
2.3.8.1* For each CCP, critical limits shall be defined and validated to identify when a process is out of
control.
2.3.9 Establish a monitoring system for each CCP
2.3.9.1* KO N° 2: Specific monitoring procedures in terms of method, frequency of measurement or
observation and recording of results, shall be documented, implemented and maintained for
each CCP, to detect any loss of control at that CCP. Each defined CCP shall be under control.
Monitoring and control of each CCP shall be demonstrated by records.
2.3.9.2 Records of CCP monitoring shall be verified by a responsible person within the company and
maintained for a relevant period.
2.3.9.3 The operative personnel in charge of the monitoring of control measures defined for CCPs and
other control measures shall have received specific training/instruction.
2.3.9.4 Control measures, other than those defined for CCPs, shall be monitored, recorded and controlled
by measurable or observable criteria.
2.3.10 Establish corrective actions
2.3.10.1 In the event that the monitoring indicates that a particular control measure defined for a CCP or
any other control measure is not under control, corrective actions shall be documented and implemented. Such corrective actions shall also take any action relating to non-conforming products
into account and identify the root cause for the loss of control of CCPs.
2.3.11 Validate the HACCP plan and establish verification procedures
2.3.11.1 Procedures of validation, including revalidation after any modification that can impact food safety,
shall be documented, implemented and maintained to ensure that the HACCP plan is suitable to
effectively control the identified hazards.
2.3.11.2*Procedures of verification shall be documented, implemented and maintained to confirm that the
HACCP plan is working correctly. Verification activities of the HACCP plan, for example:
• internal audits
• testing
• sampling
• deviations and non-conformities
• complaints
shall be performed at least once within a 12-month period or whenever significant changes occur.
The results of this verification shall be recorded and incorporated into the HACCP plan.
2.3.12 Establish documentation and record keeping
2.3.12.1 Documentation and records related to the HACCP plan, for example:
• hazard analysis
• determination of control measures defined for CCPs and other control measures
• determination of critical limits
• processes
• procedures
• outcome of control measures defined for CCPs and other control measure monitoring
activities
• training records of the personnel in charge of the CCP monitoring
• observed deviations and non-conformities and implemented corrective actions
shall be available.
3 Resource management
3.1 Human resources
3.1.1 All personnel performing work that affects product safety, quality, legality and authenticity shall
have the required competence, appropriate to their role, as a result of education, work experience
and/or training.
3.1.2 The responsibilities, competencies and job descriptions for all job titles with an impact on food
safety and product quality shall be documented, implemented and maintained. Assignment of
key roles shall be defined.
3.2 Personal hygiene
3.2.1* Risk-based requirements relating to personal hygiene shall be documented, implemented and
maintained and shall include, at a minimum, the following areas:
• hair and beards
• protective clothing (including their conditions of use in staff facilities)
• hand washing, disinfection and hygiene
• eating, drinking, smoking/vaping or other use of tobacco
• actions to be taken in case of cuts or skin abrasions
• fingernails, jewellery, false nails/eyelashes and personal belongings (including medicines)
• notification of infectious diseases and conditions impacting food safety via a medical screening
procedure.
3.2.2* KO N° 3: The requirements for personal hygiene shall be understood and applied by all relevant
personnel, contractors and visitors.
3.2.3 Compliance with personal hygiene requirements shall be monitored with a frequency based on
risks, but at least once within a 3-month period.
3.2.4 A risk-based program shall be implemented and maintained to control the effectiveness of hand
hygiene.
3.2.5 Visible jewellery (including piercing) and watches shall not be worn. Any exceptions shall have
been comprehensively evaluated based on risks and shall be effectively managed.
3.2.6 Cuts and skin abrasions shall be covered with a plaster/bandage that shall not pose contamination
risks. Plasters/bandages shall be waterproof and coloured differently from the product colour.
Where appropriate:
• plasters/bandages shall contain a metal strip
• single use gloves shall be worn.
3.2.7 In work areas where wearing headgear and/or a beard snood (coverings) is required, the hair shall
be covered completely to prevent product contamination.
3.2.8* Usage rules shall be implemented for work areas/activities where it is required to wear gloves
(coloured differently from the product colour).
3.2.9 Adequate protective clothing shall be provided in sufficient quantity for each employee.
3.2.10 All protective clothing shall be thoroughly and regularly laundered in-house, by approved contractors or by employees. This decision shall be documented and based on risks. Requirements
related to laundry shall ensure a minimum of the following:
• sufficient segregation between dirty and clean clothing at all times
• laundering conditions on water temperature and detergent dosage
• avoidance of contamination until use.
The effectiveness of the laundering shall be monitored.
3.2.11 In case of any health issue or infectious disease that may have an impact on food safety, actions
shall be taken to minimise contamination risks.
3.3 Training and instruction
3.3.1* Documented training and/or instruction programs shall be implemented with respect to the
product and process requirements and the training needs of the employees, based on their job,
and shall include:
• training contents
• training frequency
• employee tasks
• languages
• qualified trainer/tutor
• evaluation of training effectiveness.
3.3.2* The documented training and/or instruction programs shall apply to all personnel, including
seasonal and temporary workers and employees from external companies, employed in the respective work area. Upon employment, and before commencing work, they shall be trained/instructed
in accordance with the documented training/instruction programs.
3.3.3 Records of all training/instruction events shall be available, stating:
• list of participants (including their signature)
• date
• duration
• contents of training
• name of trainer/tutor.
A procedure or program shall be documented, implemented and maintained to prove the effectiveness of the training and/or instruction programs.
3.3.4 The contents of training and/or instruction shall be reviewed and updated when necessary. Special
consideration shall be given to these specific issues, at a minimum:
• food safety
• product authenticity, including food fraud
• product quality
• food defence
• food related legal requirements
• product/process modifications
• feedback from the previous documented training/instruction programs.
3.4 Staff facilities
3.4.1* Adequate staff facilities shall be provided and shall be proportional in size, equipped for the number
of personnel, and designed and controlled to minimise food safety risks. Such facilities shall be
maintained in a way to prevent contamination.
3.4.2 Product contamination risks by food and drink and/or foreign materials shall be minimised.
Consideration shall be given to food and drink from vending machines, canteen and/or brought
to work by personnel.
3.4.3 Changing rooms shall be located to allow direct access to the areas where unpacked food products
are handled. When infrastructure does not allow it, alternative measures shall be implemented and
maintained to minimise product contamination risks. Outdoor clothing and protective clothing
shall be stored separately unless alternative measures are implemented and maintained to prevent
contamination risks.
3.4.4 Toilets shall neither have direct access nor pose contamination risks to areas where products are
handled. Toilets shall be equipped with adequate hand washing facilities. The facilities shall have
adequate natural or mechanical ventilation. Mechanical airflow from a contaminated area to a
clean area shall be avoided.
3.4.5* Hand hygiene facilities shall be provided and shall address, at a minimum:
• adequate number of wash basins
• suitably located at access points to and/or within production areas
• designated for cleaning hands only.
The necessity of similar equipment in further areas (e.g. packing area) shall be based on risks.
3.4.6 Hand hygiene facilities shall provide:
• running potable water at an adequate temperature
• adequate cleaning and disinfection equipment
• adequate means for hand drying.
3.4.7 Where the processes require a higher hygiene control, the hand washing equipment shall provide
in addition:
• hand contact-free fittings
• hand disinfection
• waste container with hand contact-free opening.
3.4.8 Where needed, cleaning and disinfection facilities shall be available and used for boots, shoes and
further protective clothing.
4 Operational processes
4.1 Customer focus and contract agreement
4.1.1 A procedure shall be implemented and maintained to identify fundamental needs and expectations
of customers. The feedback from this process shall be used as input for the company’s continuous
improvement.
4.1.2 All requirements related to food safety and product quality, within the customer agreements, and
any revision of these clauses, shall be communicated to, and implemented by each relevant
department.
4.1.3* KO N° 4: Where there are customer agreements related to:
• product recipe (including raw materials characteristics)
• process
• technological requirements
• testing and monitoring plans
• packaging
• labelling
these shall be complied with.
4.1.4 In accordance with customer requirements, the senior management shall inform their affected
customers, as soon as possible, of any issue related to product safety or legality, including deviations
and non-conformities identified by competent authorities.
4.2 Specifications and formulas
4.2.1 Specifications
4.2.1.1* Specifications shall be documented and implemented for all finished products. They shall be up
to date, unambiguous and in compliance with legal and customer requirements.
4.2.1.2 A procedure to control the creation, approval and amendment of specifications shall be documented,
implemented and maintained and shall include, where required, the acceptance of the customer(s).
Where required by customers, product specifications shall be formally agreed.
This procedure shall include the update of finished product specifications in case of any modification
related to:
• raw materials
• formulas/recipes
• processes which impact the finished products
• packaging materials which impact the finished products.
4.2.1.3* KO N° 5: Specifications shall be documented and implemented for all raw materials (ingredients,
additives, packaging materials, rework). Specifications shall be up to date, unambiguous and
in compliance with legal requirements and, if defined, with customer requirements.
4.2.1.4 Specifications and/or their contents shall be available on-site for all relevant personnel.
4.2.1.5* Where products are requested to be labelled and/or promoted with a claim or where certain
methods of treatment or production are excluded, measures shall be implemented to demonstrate
compliance with such a statement.
4.3 Product development/Product modification/Modification of production
processes
4.3.1 A procedure for the development or modification of products and/or processes shall be documented,
implemented and maintained and shall include, at a minimum, a hazard analysis and assessment
of associated risks.
4.3.2* The procedure shall ensure that labelling complies with current legislation of the destination
country/ies and customer requirements.
4.3.3* The development and/or modification process shall result in specifications about formulation,
rework, packaging materials, manufacturing processes and comply with food safety, product quality,
legality, authenticity and customer requirements. This includes factory trials, product testing and
process monitoring. The progress and results of product development/modification shall be recorded.
4.3.4 Shelf life tests or appropriate validation through microbiological, chemical and organoleptic
evaluation shall be carried out and consideration shall be given to product formulation, packaging,
manufacturing and declared conditions. The shelf life shall be defined in accordance with this
evaluation.
4.3.5 Recommendations for preparation and/or instructions for use of food products related to food
safety and/or product quality shall be validated and documented.
4.3.6 Nutritional information or claims which are declared on labelling shall be validated through studies
and/or tests throughout the shelf life of the products.
4.4 Purchasing
4.4.1* A procedure for the sourcing of raw materials, semi-finished products and packaging materials
and the approval and monitoring of suppliers (internal and external) shall be documented, implemented and maintained.
This procedure shall contain, at a minimum:
• raw materials and/or suppliers’ risks
• required performance standards (e.g., certification, origin, etc.)
• exceptional situations (e.g. emergency purchase)
and, based on risks, additional criteria, for example:
• audits performed by an experienced and competent person
• testing results
• supplier reliability
• complaints
• supplier questionnaire
4.4.2 The purchased materials shall be assessed, based on risks and suppliers’ status, for food safety,
product quality, legality and authenticity. The results shall be the basis for the testing and monitoring
plans.
4.4.3* The purchasing services, which have, based on risks, an impact on food safety and product quality,
shall be evaluated to ensure they comply with defined requirements.
This shall take into account, at a minimum:
• the service requirements
• the supplier’s status (according to its assessment)
• the impact of the service on the finished products.
4.4.4* Where a part of the product processing and/or primary packing and/or labelling is outsourced,
this shall be documented in the food safety and quality management system and such processes
shall be controlled to guarantee that food safety, product quality, legality and authenticity are not
compromised. Control of such outsourced processes shall be identified and documented. When
required by the customer, there shall be evidence that they have been informed and have agreed
to such outsourced process.
4.4.5 An agreement shall be documented and implemented, covering the outsourced processes and
describing any arrangements made in connection with it, including in-process controls, testing
and monitoring plans.
4.4.6 Suppliers of the outsourced processes shall be approved through:
• certification to IFS Food or other GFSI recognised food safety certification standard, or
• documented supplier audit, performed by an experienced and competent person, which shall
include, at a minimum, requirements for food safety, product quality, legality and authenticity.
4.4.7 The sourcing of materials and supplier assessments shall be reviewed at least once within a 12-month
period or whenever significant changes occur. Records of the reviews and the consequential actions
of the assessment shall be documented.
4.5 Product packaging
4.5.1 * Based on risks and intended use, key parameters for the packaging materials shall be defined in
detailed specifications complying with the current relevant legislation and other relevant hazards
or risks.
Suitability of the food contact packaging materials and existence of functional barrier(s) shall be
validated for each relevant product. It shall be monitored and demonstrated by test/analysis, for
example:
• organoleptic tests
• storage tests
• chemical analyses
• migration test results.
4.5.2 For all packaging materials which could have an impact on products, declarations of compliance,
which attest compliance with legal requirements shall be documented. In the event that no specific
legal requirements are applicable, evidence shall be maintained to ensure that packaging materials
are suitable for use. This applies for packaging materials which could have an influence on raw
materials, semi-finished and finished products.
4.5.3 Used packaging and labelling shall correspond to the product being packed and shall comply with
agreed customer product specifications. Labelling information shall be legible and indelible. This
shall be monitored and documented at least at the start and end of a production run as well as at
every product changeover.
4.6 Factory location
4.6.1* Potential adverse impact on food safety and/or product quality from the factory environment (e.g.
ground, air) shall be investigated. Where risks have been identified (e.g. extremely dusty air, strong
smells), measures shall be documented, implemented and reviewed for effectiveness at least once
within a 12-month period or whenever significant changes occur.
4.7 Factory exterior
4.7.1 All external areas of the factory shall be clean, tidy, designed and maintained in a way to prevent
contamination. Where natural drainage is inadequate, a suitable drainage system shall be installed.
4.7.2 Outdoor storage shall be kept to a minimum. Where goods are stored outside, it shall be ensured
that there are no contamination risks or adverse effects on food safety and quality.
4.8 Plant layout and process flow
4.8.1 A site plan covering all buildings shall be documented and maintained and shall describe, at a
minimum, the process flow of:
• finished products
• semi-finished products, including rework
• packaging materials
• raw materials
• personnel
• waste
• water.
4.8.2* The process flow, from receipt of goods to dispatch, shall be implemented, maintained, reviewed
and where necessary, modified to ensure that the microbiological, chemical and physical contamination risks of raw materials, packaging materials, semi-finished and finished products are avoided.
The cross-contamination risks shall be minimised through effective measures.
4.8.3 In the case where areas sensitive to microbiological, chemical and physical risks, have been identified,
they shall be designed and operated to ensure product safety is not compromised.
4.8.4 Laboratory facilities and in-process controls shall not affect product safety.
4.9 Production and storage premises
4.9.1 Constructional requirements
4.9.1.1* Premises where food products are prepared, treated, processed and stored shall be designed,
constructed and maintained to ensure food safety.
4.9.2 Walls
4.9.2.1 Walls shall be designed and constructed to meet production requirements in a way to prevent
contamination, reduce condensation and mould growth, facilitate cleaning and if necessary,
disinfection.
4.9.2.2 The surfaces of walls shall be maintained in a way to prevent contamination and easy to clean;
they shall be impervious and wear-resistant to minimise product contamination risks.
4.9.2.3 The junctions between walls, floors and ceilings shall be designed to facilitate cleaning and if
necessary, disinfection.
4.9.3 Floors
4.9.3.1 Floor covering shall be designed and constructed to meet production requirements and be maintained in a way to prevent contamination and facilitate cleaning and if necessary, disinfection.
Surfaces shall be impervious and wear-resistant.
4.9.3.2 The hygienic disposal of water and other liquids shall be ensured. Drainage systems shall be
designed, constructed and maintained in a way to minimise product contamination risks (e.g. entry
of pests, areas sensitive to transmission of odour or contaminants) and shall be easy to clean.
4.9.3.3 In food handling areas, machinery and piping shall be arranged to allow waste water, if possible,
to flow directly into a drain.
Water and other liquids shall reach drainage using appropriate measures without difficulty.
Stagnation of puddles shall be avoided.
4.9.4 Ceilings/Overheads
4.9.4.1 Ceilings (or, where no ceilings exist, the inside of roofs) and overhead fixtures (including piping,
cableway, lamps, etc.) shall be designed, constructed and maintained to minimise the accumulation
of dirt and condensation and shall not pose any physical and/or microbiological contamination
risks.
4.9.4.2 Where false ceilings are used, access to the vacant area shall be provided to facilitate cleaning,
maintenance and inspection for pest control.
4.9.5 Windows and other openings
4.9.5.1 Windows and other openings shall be designed and constructed to avoid the accumulation of dirt
and shall be maintained in a way to prevent contamination.
4.9.5.2 Where there are contamination risks, windows and roof glazing shall remain closed and fixed during
production.
4.9.5.3 Where windows and roof glazing are designed to be opened for ventilation purposes, they shall
be fitted with easy to clean pest screens or other measures to prevent any contamination.
4.9.5.4 In areas where unpackaged products are handled, windows shall be protected against breakage.
4.9.6 Doors and gates
4.9.6.1 Doors and gates shall be maintained in a way to prevent contamination and be easy to clean. They
shall be designed and constructed of non-absorbent materials to avoid:
• splintering parts
• flaking paint
• corrosion.
4.9.6.2 External doors and gates shall be constructed to prevent the access of pests.
4.9.6.3 Plastic strip curtains separating areas shall be maintained in a way to prevent contamination and
be easy to clean.
4.9.7 Lighting
4.9.7.1 All production, storage, receipt and dispatch areas shall have adequate levels of light.
4.9.8 Air conditioning/Ventilation
4.9.8.1 Adequate natural and/or artificial ventilation shall be designed, constructed and maintained in all
areas.
4.9.8.2 If ventilation equipment is installed, filters and other components shall be easily accessible and
monitored, cleaned or replaced as necessary.
4.9.8.3 Air conditioning equipment and artificially generated airflow shall not compromise product safety
and quality.
4.9.8.4 Dust extraction equipment shall be designed, constructed and maintained in areas where considerable amounts of dust are generated.
4.9.9 Water
4.9.9.1* Water which is used for hand washing, cleaning and disinfection, or as an ingredient in the production
process shall be of potable quality at the point of use and supplied in sufficient quantities.
4.9.9.2 The quality of water (including recycled water), steam or ice shall be monitored following a riskbased sampling plan.
4.9.9.3 Recycled water, which is used in the process, shall not pose contamination risks.
4.9.9.4 Non-potable water shall be transported in separate, properly marked piping. Such piping shall
neither be connected to the potable water system nor allow the possibility of reflux, to prevent
contamination of potable water sources or factory environment.
4.9.10 Compressed air and gases
4.9.10.1*The quality of compressed air that comes in direct contact with food or food contact materials
shall be monitored based on risks. Compressed air shall not pose contamination risks.
4.9.10.2 Gases that come in direct contact with food or food contact materials, shall demonstrate safety
and quality for the intended use.
4.10 Cleaning and disinfection
4.10.1* Risk-based cleaning and disinfection schedules shall be validated, documented and implemented.
These shall specify:
• objectives
• responsibilities
• the products used and their instructions for use
• dosage of cleaning and disinfection chemicals
• the areas and timeslots for cleaning and disinfection activities
• cleaning and disinfection frequency
• Cleaning In Place (CIP) criteria, if applicable
• documentation requirements
• hazard symbols (if necessary).
4.10.2 Cleaning and disinfection activities shall be implemented and shall result in effectively cleaned
premises, facilities and equipment.
4.10.3 Cleaning and disinfection activities shall be documented and such records shall be verified by a
responsible designated person in the company.
4.10.4* Only competent personnel shall perform cleaning and disinfection activities. The personnel shall
be trained and retrained to carry out the cleaning and disinfection schedules.
4.10.5* The intended use of cleaning and disinfection equipment shall be clearly specified. It shall be used
and stored in a way to avoid contamination.
4.10.6 Safety data sheets and instructions for use shall be available on-site for cleaning and disinfection
chemicals. Personnel responsible for cleaning and disinfection activities shall be able to demonstrate
their knowledge of such instructions.
4.10.7 The effectiveness of the cleaning and disinfection measures shall be verified. The verification shall
rely on a risk-based sampling schedule and shall consider, one or several actions, for example:
• visual inspection
• rapid testing
• analytical testing methods.
Resultant actions shall be documented.
4.10.8 Cleaning and disinfection schedules shall be reviewed and modified in the event that changes
occur to products, processes or cleaning and disinfection equipment, if necessary.
4.10.9 Where a company hires a third-party service provider for cleaning and disinfection activities in
production areas, all above-mentioned requirements shall be documented in the service
contract.
4.11 Waste management
4.11.1* A waste management procedure shall be documented, implemented and maintained to prevent
cross contamination.
4.11.2 All local legal requirements for waste disposal shall be met.
4.11.3 Food waste and other waste shall be removed as quickly as possible from areas where food is
handled. The accumulation of waste shall be avoided.
4.11.4 Waste collection containers shall be clearly marked, suitably designed and maintained, easy to
clean, and where necessary, disinfected.
4.11.5 If a company decides to separate food waste and to reintroduce it into the feed supply chain,
measures or procedures shall be implemented to prevent contamination or deterioration of this
material.
4.11.6 Waste shall be collected in separate containers in accordance with the intended means of disposal.
Such waste shall be disposed of by authorised third-parties only. Records of waste disposal shall
be kept by the company.
4.12 Foreign material and chemical risk mitigation
4.12.1* KO N° 6: Based on risks, procedures shall be documented, implemented and maintained to
prevent contamination with foreign materials. Contaminated products shall be treated as
non-conforming products.
4.12.2 The products being processed shall be protected against physical contamination, which includes
but is not limited to:
• environmental contaminants
• oils or dripping liquids from machinery
• dust spills.
Special consideration shall also be given to product contamination risks caused by:
• equipment and utensils
• pipes
• walkways
• platforms
• ladders.
If, for technological characteristics and/or needs, it is not possible to protect the products, appropriate
control measures shall be implemented.
4.12.3 All chemicals within the site shall be fit for purpose, labelled, stored and handled in a way not to
pose contamination risks.
4.12.4 Where metal and/or other foreign material detectors are required, they shall be installed to ensure
maximum efficiency of detection to prevent subsequent contamination. Detectors shall be subjected
to maintenance to avoid malfunction at least once within a 12-month period, or whenever significant
changes occur.
4.12.5 The accuracy of all equipment and methods designed to detect and/or eliminate foreign materials
shall be specified. Functionality tests of such equipment and methods shall be carried out on a
risk-based frequency. In case of malfunction or failure, the impact on products and processes shall
be assessed.
4.12.6 Potentially contaminated products shall be isolated. Access and actions for the further handling
or testing of these isolated products shall only be carried out by authorised personnel.
4.12.7 In areas where raw materials, semi-finished and finished products are handled, the use of glass
and/or brittle materials shall be excluded; however where the presence of glass and/or brittle
materials cannot be avoided, the risks shall be controlled and the glass and/or brittle materials
shall be clean and pose no risks to product safety.
4.12.8 Risk-based measures shall be implemented and maintained for the handling of glass packaging,
glass containers or other kinds of containers in the production process (turn over, blow, rinse, etc.).
After this process step, there shall be no further contamination risks.
4.12.9 Procedure(s) shall be documented, implemented and maintained describing the measures to be
taken in case of glass breakage and/or brittle materials. Such measures shall include identifying
the scope of goods to be isolated, specifying authorised personnel, cleaning and if necessary,
disinfection of the production environment and releasing the production line for continued
production.
4.12.10 Breakages of glass and brittle materials shall be recorded. Exceptions shall be justified and
documented.
4.12.11 Where visual inspection is used to detect foreign materials, the employees shall be trained and
operative changes shall be performed at an appropriate frequency to maximise the effectiveness
of the process.
4.12.12 In areas where raw materials, semi-finished and finished products are handled, the use of wood
shall be excluded; however, where the presence of wood cannot be avoided, the risks shall be
controlled and the wood shall be clean and pose no risks to product safety.
4.13 Pest monitoring and control
4.13.1 Site premises and equipment shall be designed, built and maintained to prevent pest infestation.
4.13.2* Risk-based pest control measures shall be documented, implemented and maintained. They shall
comply with local legal requirements and shall take into account, at a minimum:
• factory environment (potential and targeted pests)
• type of raw material/finished products
• site plan with area for application (bait map)
• constructional designs susceptible for pest activity, for example ceilings, cellars, pipes, corners
• identification of the baits on-site
• responsibilities, in-house/external
• agents used and their instructions for use and safety
• frequency of inspections
• rented storage if applicable.
4.13.3 Where a company hires a third-party service provider for pest control, all above-mentioned requirements shall be documented in the service contract. A competent person at the company shall be
appointed to monitor the pest control activities. Even if the pest control service is outsourced,
responsibilities for the necessary actions (including ongoing supervision of pest control activities)
shall remain within the company.
4.13.4 Pest control inspections and resulting actions shall be documented. Implementation of actions
shall be monitored and recorded. Any infestation shall be documented and control measures taken.
4.13.5 Baits, traps and insect exterminators shall be fully functioning, sufficient in number, designed for
purpose, placed in appropriate positions and used in a way to avoid contamination.
4.13.6 Incoming deliveries shall be inspected on arrival for the presence of pests. Any findings shall be
recorded.
4.13.7 The effectiveness of the pest control measures shall be monitored, including trend analysis, to
allow timely appropriate actions. Records of this monitoring shall be available.
4.14 Receipt and storage of goods
4.14.1* All incoming goods, including packaging materials and labels, shall be checked for compliance
with specifications and a determined risk-based monitoring plan. The monitoring plan shall be
justified by risk assessment. Records of those inspections shall be available.
4.14.2* A system shall be implemented and maintained to ensure storage conditions of raw materials,
semi-finished, finished products and packaging materials, correspond to product specifications,
and do not have any negative impact on other products.
4.14.3 Raw materials, packaging materials, semi-finished and finished products shall be stored to minimise
contamination risks or any other negative impact.
4.14.4 Adequate storage facilities shall be available for the management and storage of working materials,
process aids and additives. The personnel responsible for the management of storage facilities
shall be trained.
4.14.5* All products shall be identified. Use of products shall be undertaken in accordance with the principles
of First In/First Out and/or First Expired/First Out.
4.14.6 Where a company hires a third-party storage service provider, the service provider shall be certified
to IFS Logistics or any other GFSI recognised certification standard covering the respective scope
of activity. If not, all relevant requirements equivalent to the company’s own storage practices shall
be fulfilled and this shall be defined in the respective contract.
4.15 Transport
4.15.1* The conditions inside the vehicles related to the absence of, for example:
• strange smells
• high dust load
• adverse humidity
• pests
• mould
shall be checked before loading and documented to ensure compliance with the defined
conditions.
4.15.2 Where goods are transported at certain temperatures, the temperature inside the vehicles shall
be checked and documented before loading.
4.15.3 Procedures to prevent contamination during transport, including loading and unloading, shall be
documented, implemented and maintained. Different categories of goods (food/non-food) shall
be taken into consideration, if applicable.
4.15.4 Where goods are transported at certain temperatures, maintaining the appropriate range of
temperatures during transport shall be ensured and documented.
4.15.5 Risk-based hygiene requirements for all transport vehicles and equipment used for loading/unloading
(e.g. hoses of silo installations) shall be implemented. Measures taken shall be recorded.
4.15.6 The loading/unloading areas shall be appropriate for their intended use. They shall be constructed
in a way that:
• the risks of pest intake are mitigated
• products are protected from adverse weather conditions
• accumulation of waste is avoided
• condensation and growth of mould are prevented
• cleaning and if necessary, disinfection can be easily undertaken.
4.15.7 Where a company hires a third-party transport service provider, the service provider shall be certified
for IFS Logistics or any other GFSI recognised certification standard covering the respective scope
of activity. If not, all relevant requirements equivalent to the company’s own transport practices
shall be fulfilled and this shall be defined in the respective contract.
4.16 Maintenance and repair
4.16.1* A maintenance plan shall be documented, implemented and maintained, that covers all critical
equipment (including transport and storage premises) to ensure food safety, product quality and
legality. This applies both to internal maintenance activities and service providers. The plan shall
include responsibilities, priorities and due dates.
4.16.2 Food safety, product quality, legality and authenticity shall be ensured during and after maintenance
and repair work. Records of maintenance and repair work shall be kept.
4.16.3 All materials used for maintenance and repair shall be fit for the intended use and shall not pose
contamination risks.
4.16.4 Failures and malfunctions of premises and equipment (including transport) that are essential for
food safety and product quality shall be identified, documented and reviewed to enable prompt
actions and to improve the maintenance plan.
4.16.5 Temporary repairs shall be carried out to avoid compromising food safety and product quality.
Such work shall be documented and a short-term deadline set for eliminating the issue.
4.16.6 Where a company hires a third-party maintenance and repair service provider, all the company
requirements regarding material, equipment and operational rules shall be defined, documented
and maintained in the service contract, to prevent any product contamination.
4.17 Equipment
4.17.1* Equipment shall be suitably designed and defined for the intended use. Before commissioning
new equipment, compliance with food safety, product quality, legality, authenticity and customer
requirements shall be validated.
4.17.2 For all equipment and utensils which could have an impact on the product, evidence shall be
documented to demonstrate compliance with legal requirements.
In case no specific legal requirements are in place, evidence shall be available, for example:
• certificate of conformity
• technical specifications
• manufacturer’s self-declaration
to demonstrate that they are suitable for the intended use.
4.17.3 Equipment shall be located to allow effective cleaning, disinfection and maintenance operations.
4.17.4 All product equipment shall be in a condition that does not compromise food safety and product
quality.
4.17.5 In the event of changes to equipment, the process characteristics shall be reviewed to ensure that
food safety, product quality, legality, authenticity and customer requirements are complied with.
4.18 Traceability
4.18.1* KO N° 7: A traceability system shall be documented, implemented and maintained that
enables the identification of product lots and their relation to batches of raw materials, and
food contact packaging materials, and/or materials carrying legal and/or relevant food safety
information. The traceability system shall incorporate all relevant records of:
• receipt
• processing at all steps
• use of rework
• distribution.
Traceability shall be ensured and documented until delivery to the customer.
4.18.2* The traceability system, including mass balance, shall be tested at least once within a 12-month
period or whenever significant changes occur. The test samples shall reflect the complexity of the
company’s product range. The test records shall demonstrate upstream and downstream traceability
(from delivered products to raw materials, and vice versa).
4.18.3 The traceability from the finished products to the raw materials and to the customers shall be
performed within four (4) hours maximum. Test results, including the timeframe for obtaining the
information, shall be recorded and, where necessary, actions shall be taken. Timeframe objectives
shall be in compliance with customer requirements, if less than four (4) hours are required.
4.18.4 Labelling of semi-finished or finished product lots shall be made at the time when the goods are
directly packed to ensure clear traceability of goods. Where goods are labelled at a later time, the
temporarily stored goods shall have a specific lot labelling. Shelf life (e.g. best before date) of
labelled goods shall be defined using the original production batch.
4.18.5 If required by the customer, identified representative samples of the manufacturing lot or batch
number shall be stored appropriately and kept until expiration of the “Use by” or “Best before” date
of the finished products and, if necessary, for a determined period beyond this date.
4.19 Allergen risk mitigation
4.19.1 For all raw materials, a risk assessment shall be performed to identify allergens requiring declarations,
including accidental or technically unavoidable cross-contaminations of legally declared allergens
and traces. This information shall be available and relevant to the country/ies of sale of the finished
products and shall be documented and maintained for all raw materials. A continuously up to date
listing of all raw materials containing allergens used on the premises shall be maintained. This shall
also identify all blends and formulas to which such raw materials containing allergens are added.
4.19.2* Risk-based measures shall be implemented and maintained from receipt to dispatch, to ensure
that potential cross contamination of products by allergens is minimised. The potential cross
contamination risks shall be considered, related to, at a minimum:
• environment
• transport
• storage
• raw materials
• personnel (including contractors and visitors).
Implemented measures shall be monitored.
4.19.3 Finished products containing allergens that require declarations shall be declared in accordance
with legal requirements. Accidental or technically unavoidable cross-contaminations of legally
declared allergens and traces shall be labelled. The decision shall be risk-based. The potential
cross-contamination with allergens from raw materials processed in the company shall also be
taken into account on the product label.
4.20 Food fraud
4.20.1 The responsibilities for a food fraud vulnerability assessment and mitigation plan shall be defined.
The responsible person(s) shall have the appropriate specific knowledge.
4.20.2* A documented food fraud vulnerability assessment, including assessment criteria, shall be documented, implemented and maintained. The scope of the assessment shall cover all raw materials,
ingredients, packaging materials and outsourced processes, to determine the risks of fraudulent
activity in relation to substitution, mislabelling, adulteration or counterfeiting.
4.20.3 A food fraud mitigation plan shall be documented, implemented and maintained with reference
to the vulnerability assessment, and shall include the testing and monitoring methods.
4.20.4* The food fraud vulnerability assessment shall be reviewed, at least once within a 12-month period
or whenever significant changes occur. If necessary, the food fraud mitigation plan shall be revised/
updated accordingly.
4.21 Food defence
4.21.1 The responsibilities for food defence shall be defined. The responsible person(s) shall have the
appropriate specific knowledge.
4.21.2* A food defence procedure and plan shall be documented, implemented and maintained to identify
potential threats and define food defence measures. This shall include, at a minimum:
• legal requirements
• identification of critical areas and/or practices and policy of access by employees
• visitors and contractors
• how to manage external inspections and regulatory visits
• any other appropriate control measures.
4.21.3 The food defence plan shall be tested for effectiveness and reviewed at least once within a 12-month
period or whenever significant changes occur.
5 Measurements, analyses, improvements
5.1 Internal audits
5.1.1* KO N° 8: An effective internal audit program shall be documented, implemented and maintained
and shall ensure, at a minimum, that all the requirements of the IFS Standard are audited. This
activity shall be planned within a 12-month period and its execution shall not exceed 15 months.
The company shall have a risk assessment in place where activities, which are critical to food
safety and product quality shall be audited more frequently.
It shall also apply to off-site storage locations owned or rented by the company.
5.1.2 The auditors shall be competent and independent from the audited department.
5.1.3 Internal audits shall be documented and results communicated to the senior management and to
the persons responsible for the concerned activities. Compliances, deviations and non-conformities
shall be documented and communicated to the relevant persons.
5.2 Site factory inspections
5.2.1* Site and factory inspections shall be planned and carried out for certain topics, like for example:
• constructional status of production and storage premises
• external areas
• product control during processing
• hygiene during processing and within the infrastructure
• foreign material hazards
• personal hygiene.
The frequency of inspections shall be based on risks and on the history of previous results.
5.3 Process validation and control
5.3.1 The criteria for process validation and control shall be defined.
5.3.2 Process parameters (temperature, time, pressure, chemical properties, etc.) which are essential to
ensure the food safety and product quality shall be monitored, recorded continuously and/or at
appropriate intervals and secured against unauthorised access and/or change.
5.3.3* All rework operations shall be validated, monitored and documented. These operations shall not
affect the food safety and product quality requirements.
5.3.4 Procedures shall be documented, implemented and maintained for prompt notification, recording
and monitoring of equipment malfunction and process deviations.
5.3.5 Process validation shall be performed using the collected data that is relevant for food safety and
the processes. If substantial modifications occur, a re-validation shall be carried out.
5.4 Calibration, adjustment and checking of measuring and monitoring devices
5.4.1* Measuring and monitoring devices required to ensure compliance with food safety and product
quality requirements shall be identified and recorded. Their calibration status shall be recorded.
Measuring and monitoring devices shall be legally approved, if required by current relevant
legislation.
5.4.2* All measuring devices shall be checked, monitored, adjusted and calibrated at defined intervals,
in accordance with defined, recognised standard/methods and within relevant limits of the
process parameter values. The results shall be documented.
5.4.3 All measuring devices shall be used exclusively for their defined purpose. Where the results of
measurements or the status of the device indicate a malfunction, the device in question shall be
immediately repaired or replaced. Where a malfunction has been identified, the impact on processes
and products shall be assessed to identify whether non-conforming products have been
processed.
5.5 Quantity control monitoring
5.5.1* Compliance criteria to control lot quantity shall be defined. A system on frequency and methodology
for quantity control shall be implemented and maintained to meet the legal requirements of the
destination country/ies and customer specifications.
5.5.2 Quantity control monitoring shall be implemented and recorded, according to a sampling plan
which ensures a proper representation of the manufacturing lot. The results from this monitoring
shall be compliant with defined criteria for all products ready to be delivered.
5.6 Product testing and environmental monitoring
5.6.1* Testing and monitoring plans for internal and external analyses shall be documented and implemented and shall be risk-based to ensure that product safety, quality, legality, authenticity and
specific customer requirements are met. The plans shall cover a minimum of:
• raw materials
• semi-finished products (if applicable)
• finished products
• packaging materials
• contact surfaces of processing equipment
• relevant parameters for environmental monitoring.
All test results shall be recorded.
5.6.2* Based on risks, the criteria for environmental monitoring program shall be documented, implemented
and maintained
5.6.3* Analyses which are relevant for food safety shall preferably be performed by laboratories with
appropriate accredited programs/methods (ISO/IEC 17025). If the analyses are performed internally
or by a laboratory without the appropriate accredited programs/methods, the results shall be
cross-checked with test results from laboratories accredited to these programs/methods (ISO/IEC
17025) at least once within a 12-month period, or whenever significant changes occur.
5.6.4 Procedures shall be documented, implemented and maintained to ensure the reliability of the
results from internal analyses, based on officially recognised analysis methods. This shall be demonstrated by ring tests or other proficiency tests.
5.6.5 Results of analyses shall be evaluated in a timely manner by competent personnel. Immediate
corrections shall be implemented for any unsatisfactory results. Based on risks and legal requirements,
the frequency for review of the testing and monitoring plan results shall be defined in order to
identify trends. When unsatisfactory trends are identified, the impact on processes and products
as well as the need for actions shall be assessed.
5.6.6 Where internal analyses or controls are undertaken, these shall be carried out in accordance with
defined procedures, by competent and approved personnel, in defined areas or laboratories, using
appropriate equipment.
5.6.7 For monitoring of the quality of the finished product, internal organoleptic tests shall be carried
out. These tests shall be in accordance with specifications and related to the impact on respective
parameters of product characteristics. The results of these tests shall be documented.
5.6.8 The testing and monitoring plans shall be regularly reviewed and updated, based on results,
changes to legislation or issues that may have an impact on product safety, quality, legality and
authenticity.
5.7 Product release
5.7.1* A procedure for quarantine (blocking/hold) shall be documented, implemented and maintained
to ensure that only raw materials, semi-finished and finished products, and packaging materials,
complying with food safety, product quality, legality, authenticity and customer requirements, are
processed and delivered.
5.8 Management of complaints from authorities and customers
5.8.1* A procedure shall be documented, implemented and maintained for the management of product
complaints and of any written notification from the competent authorities – within the framework
of official controls –, any ordering action or measure to be taken when non-compliance is
identified.
5.8.2* All complaints shall be recorded, be readily available and assessed by competent staff.
Where it is justified, actions shall be taken immediately.
5.8.3 Complaints shall be analysed with a view to implementing actions to avoid the recurrence of the
deviations and/or non-conformities.
5.8.4 The results of complaint data analysis shall be made available to the relevant responsible persons.
5.9 Management of product recalls, product withdrawals and incidents
5.9.1* KO N° 9: An effective procedure shall be documented, implemented and maintained for the
management of recalls, withdrawals, incidents and potential emergency situations with an
impact on food safety, product quality, legality and authenticity. It shall include, at a
minimum:
• the assignment of responsibilities
• the training of the responsible persons
• the decision-making process
• the nomination of a person, authorised by the company and permanently available, to initiate
the necessary process in a timely manner
• an up-to-date alert contact list including customer information, sources of legal advice,
available contacts
• a communication plan including customers, authorities and where applicable, consumers.
5.9.2* The procedure shall be subject to internal testing for recall/withdrawal, by covering the end-to-end
process. This activity shall be planned within a 12-month period and its execution shall not exceed
15 months. The outcome of the test shall be reviewed for continuous improvement.
5.10 Management of non-conforming products
5.10.1* A procedure shall be documented, implemented and maintained for the management of all
non-conforming raw materials, semi-finished products, finished products, processing equipment
and packaging materials. This shall include, at a minimum:
• defined responsibilities
• isolation/quarantine procedures
• risk assessment
• identification including labelling
• decision about the further usage like release, rework/reprocessing, blocking, quarantine, rejection/
disposal.
5.10.2 The procedure for the management of non-conforming products shall be understood and applied
by all relevant employees.
5.10.3 Where non-conforming products are identified, immediate actions shall be taken to ensure that
food safety and product quality requirements are complied with.
5.10.4 Finished products (including packaging) that are out of specification shall not be placed on the
market under the corresponding label unless a written approval of the brand owner is available.
5.11 Management of deviations, non-conformities, corrections and corrective
actions
5.11.1* A procedure for the management of corrections and corrective actions shall be documented,
implemented and maintained for the recording, analysis, and communication to the relevant
persons of deviations, non-conformities and non-conforming products, with the objective to close
the deviations and/or non-conformities and avoid recurrences via corrective actions. This shall
include a root cause analysis, at least for deviations and non-conformities related to safety, legality,
authenticity and/or recurrence of deviations and non-conformities.
5.11.2 Where deviations and non-conformities are identified, corrections shall be implemented.
5.11.3* KO N° 10: Corrective actions shall be formulated, documented and implemented as soon as
possible to avoid the further occurrence of deviations and non-conformities. The responsibilities
and the timescales for corrective actions shall be defined.
5.11.4 The effectiveness of the implemented corrections and corrective actions shall be assessed and the
results of the assessment documented






















"""

def get_groq_client():
    """Initialize and return a Groq client with the API key."""
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    urls = [
        "https://raw.githubusercontent.com/m00n69/nconfgroq/main/ifs_food_v8_audit_checklist_guideline_v1_en_1706090430.txt"
    ]
    documents = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            documents.append(response.text)
        else:
            st.error(f"Failed to load document from: {url}. Status code: {response.status_code}")
    if not documents:
        st.error("No documents loaded successfully.")

    # Add the long text as additional document content
    documents.append(long_text_placeholder)

    return documents

def generate_response(user_input, documents):
    """Generate a response to the user query using Groq and the loaded documents."""
    client = get_groq_client()

    system_instruction = """
    Utilisez exclusivement les informations du contexte fourni, en particulier les documents chargés, pour générer des réponses. Les réponses doivent être en français, basées uniquement sur les données fournies sans extrapolation. Aucun lien externe ou référence directe à des sources non incluses dans les documents ne doit être utilisé. Vérifiez la précision des clauses mentionnées par rapport au fichier ifsv8.txt en utilisant les autres documents comme références complémentaires.
    """

    messages = [
        {"role": "user", "content": user_input},
        {"role": "system", "content": system_instruction}
    ]
    for doc in documents:
        messages.append({"role": "assistant", "content": doc})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192"
    )

    return chat_completion.choices[0].message.content

def main():
    st.title("Question sur les normes IFS v8")

    documents = load_documents()

    if documents:
        user_input = st.text_area("Posez votre question ici:", height=300)
        if st.button("Envoyer"):
            with st.spinner('Génération de la réponse en cours...'):
                response = generate_response(user_input, documents)
                st.write(response)
    else:
        st.error("Document loading failed, cannot proceed.")

if __name__ == "__main__":
    main()
