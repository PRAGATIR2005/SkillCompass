# ============================================================
# SKILLCOMPASS - STAGE 1 ASSESSMENT QUESTIONS
# Post-10th Grade → Stream Choice
# ============================================================


# ------------------------------------------------------------
# RESPONSE OPTIONS
# ------------------------------------------------------------

ABILITY_OPTIONS = [
    {
        "label": "Very Low",
        "score": 1
    },
    {
        "label": "Low",
        "score": 3
    },
    {
        "label": "Average",
        "score": 5
    },
    {
        "label": "High",
        "score": 7
    },
    {
        "label": "Very High",
        "score": 9
    }
]


INTEREST_OPTIONS = [
    {
        "label": "Strongly Dislike / Not Interested",
        "score": 1
    },
    {
        "label": "Dislike / Slightly Interested",
        "score": 3
    },
    {
        "label": "Neutral",
        "score": 5
    },
    {
        "label": "Like / Interested",
        "score": 7
    },
    {
        "label": "Strongly Like / Very Interested",
        "score": 9
    }
]


# ------------------------------------------------------------
# STAGE 1 QUESTIONS
# ------------------------------------------------------------

STAGE1_QUESTIONS = [

    # ========================================================
    # MATHEMATICAL APTITUDE
    # ========================================================

    {
        "id": 1,
        "question": (
            'How confidently can you solve school mathematics problems involving algebra, equations, ratios, or percentages?'
        ),
        "feature": "math_aptitude",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 2,
        "question": (
            'When a mathematics question has several steps, how well can you choose a method and check whether your answer makes sense?'
        ),
        "feature": "math_aptitude",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },



    # ========================================================
    # PHYSICS INTEREST
    # ========================================================

    {
        "id": 3,
        "question": (
            'How interested are you in learning how force, motion, electricity, or energy explains things you observe around you?'
        ),
        "feature": "physics_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 4,
        "question": (
            'If a physics lesson includes a practical demonstration, how interested are you in understanding the science behind the result?'
        ),
        "feature": "physics_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },



    # ========================================================
    # BIOLOGY INTEREST
    # ========================================================

    {
        "id": 5,
        "question": (
            'How interested are you in learning how the human body works, including organs, health, and disease prevention?'
        ),
        "feature": "biology_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 6,
        "question": (
            'How interested are you in studying living things, heredity, plants, animals, or ecosystems?'
        ),
        "feature": "biology_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },



    # ========================================================
    # CHEMISTRY INTEREST
    # ========================================================

    {
        "id": 7,
        "question": (
            'How interested are you in understanding why substances react, how mixtures change, or how materials are formed?'
        ),
        "feature": "chemistry_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 8,
        "question": (
            'How interested are you in learning about atoms, elements, compounds, and the properties of different materials?'
        ),
        "feature": "chemistry_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },



    # ========================================================
    # LOGICAL REASONING
    # ========================================================

    {
        "id": 9,
        "question": (
            'How well can you identify a pattern in a puzzle or sequence and use it to work out the next step?'
        ),
        "feature": "logical_reasoning",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 10,
        "question": (
            'When a school problem gives you several clues, how confidently can you compare them and select a logical answer?'
        ),
        "feature": "logical_reasoning",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },



    # ========================================================
    # VERBAL & LANGUAGE SKILL
    # ========================================================

    {
        "id": 11,
        "question": (
            'How confidently can you explain a school topic in your own words in an essay, presentation, or discussion?'
        ),
        "feature": "verbal_language_skill",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 12,
        "question": (
            'How interested are you in reading, writing, debating, learning languages, or analysing stories and texts?'
        ),
        "feature": "verbal_language_skill",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },



    # ========================================================
    # SOCIAL SCIENCE INTEREST
    # ========================================================

    {
        "id": 13,
        "question": (
            'How interested are you in studying history, geography, government, economics, or how societies develop?'
        ),
        "feature": "social_science_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 14,
        "question": (
            'How interested are you in discussing social issues and understanding how laws, policies, and communities affect people?'
        ),
        "feature": "social_science_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },



    # ========================================================
    # CREATIVITY & ARTS INTEREST
    # ========================================================

    {
        "id": 15,
        "question": (
            'How interested are you in creating original artwork, visual designs, music, stories, or other creative work?'
        ),
        "feature": "creativity_arts_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 16,
        "question": (
            'When given an open-ended school project, how much do you enjoy developing your own design or creative approach?'
        ),
        "feature": "creativity_arts_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },



    # ========================================================
    # BUSINESS & FINANCE INTEREST
    # ========================================================

    {
        "id": 17,
        "question": (
            'How interested are you in learning how businesses earn revenue, manage costs, and make financial decisions?'
        ),
        "feature": "business_finance_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 18,
        "question": (
            'How interested are you in planning a small business idea, deciding what to sell, or understanding customers?'
        ),
        "feature": "business_finance_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },



    # ========================================================
    # HANDS-ON PRACTICAL PREFERENCE
    # ========================================================

    {
        "id": 19,
        "question": (
            'How much do you enjoy building models, assembling parts, repairing objects, or learning by working with your hands?'
        ),
        "feature": "hands_on_practical_preference",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 20,
        "question": (
            'For a school science or technology topic, how much do you prefer experiments and practical activities over only reading theory?'
        ),
        "feature": "hands_on_practical_preference",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },


]


# ------------------------------------------------------------
# HELPER FUNCTION
# ------------------------------------------------------------

def get_stage1_questions():
    """
    Return all Stage 1 assessment questions.
    """
    return STAGE1_QUESTIONS

# ============================================================
# SKILLCOMPASS - STAGE 2 ASSESSMENT QUESTIONS
# Post-12th / PUC → Higher Education Field
# ============================================================

STAGE2_QUESTIONS = [
    {
        "id": 1,
        "question": 'How confidently could you handle the mathematics used in an engineering course, such as equations, functions, or quantitative problem-solving?',
        "feature": "math_score",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },
    {
        "id": 2,
        "question": 'How interested are you in using biology, chemistry, and other science concepts to understand health, living systems, or natural processes?',
        "feature": "science_aptitude",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },
    {
        "id": 3,
        "question": 'When a technical, legal, or case-based problem has several possible explanations, how well can you compare evidence and reason toward a conclusion?',
        "feature": "logical_reasoning",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },
    {
        "id":4,
        "question": 'How confidently could you explain an assignment, case analysis, project proposal, or technical idea to a group?',
        "feature": "verbal_communication_skill",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },
    {
        "id": 5,
        "question": 'How effectively can you learn and recall detailed material, such as scientific terms, legal concepts, procedures, or course definitions?',
        "feature": "memorization_strength",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },
    {
        "id": 6,
        "question": 'How interested are you in designing the appearance and usability of a product, interface, space, or visual communication project?',
        "feature": "creativity_design_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },
    {
        "id": 7,
        "question": 'How much would you enjoy coordinating a college team project, assigning tasks, and helping the group meet a deadline?',
        "feature": "leadership_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },
    {
        "id": 8,
        "question": 'How interested are you in analysing a business case, planning a budget, or deciding how an organisation should use its resources?',
        "feature": "business_acumen_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },
    {
        "id": 9,
        "question": 'How interested are you in examining a legal case, debating rights and responsibilities, or understanding how laws protect people?',
        "feature": "social_justice_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },
    {
        "id": 10,
        "question": 'How much would you enjoy practical coursework such as building a prototype, conducting a lab activity, testing a device, or using technical tools?',
        "feature": "technical_hands_on_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    }
,

    {
        "id": 11,
        "question": 'How confidently could you interpret graphs, numerical data, or calculations that appear in engineering, economics, or research coursework?',
        "feature": "math_score",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 12,
        "question": 'How interested are you in investigating a scientific question by forming an explanation, examining evidence, and drawing a conclusion?',
        "feature": "science_aptitude",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 13,
        "question": 'How well can you break a complicated assignment or case study into smaller questions and solve them in a logical order?',
        "feature": "logical_reasoning",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 14,
        "question": 'How comfortable are you writing a structured report and presenting its main findings clearly to classmates or instructors?',
        "feature": "verbal_communication_skill",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 15,
        "question": 'How well can you retain detailed information and retrieve the right facts when answering exam questions or applying a procedure?',
        "feature": "memorization_strength",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 16,
        "question": 'How interested are you in sketching alternatives, testing layouts, or improving the user experience of a product or digital application?',
        "feature": "creativity_design_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 17,
        "question": 'How much would you enjoy representing a student team, organising a college event, or guiding a group toward a shared outcome?',
        "feature": "leadership_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 18,
        "question": 'How interested are you in comparing costs, customer needs, and expected benefits before recommending a business decision?',
        "feature": "business_acumen_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 19,
        "question": 'How interested are you in analysing a real-world legal or social problem from different viewpoints before deciding what is fair?',
        "feature": "social_justice_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 20,
        "question": 'How much would you enjoy learning through labs, simulations, prototypes, clinical-style practical exercises, or hands-on technical projects?',
        "feature": "technical_hands_on_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    }
]


def get_stage2_questions():
    """Return all Stage 2 assessment questions."""
    return STAGE2_QUESTIONS

def get_stage3_questions():
    """Return all Stage 3 assessment questions."""
    return STAGE3_QUESTIONS

# ============================================================
# SKILLCOMPASS - STAGE 3 ASSESSMENT QUESTIONS
# Working Professional → Career Switch Guidance
# ============================================================

STAGE3_QUESTIONS = [

    # ========================================================
    # EXPERIENCE LEVEL
    # ========================================================

    {
        "id": 1,
        "question": (
            'How clearly can you describe the length and breadth of your professional experience, including the responsibilities you have handled independently?'
        ),
        "feature": "experience_level",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # ========================================================
    # CURRENT SKILL RELEVANCE
    # ========================================================

    {
        "id": 2,
        "question": (
            'How closely do your current skills match the requirements of the roles you might apply for in your present or a related industry?'
        ),
        "feature": "current_skill_relevance",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # ========================================================
    # JOB SATISFACTION
    # ========================================================

    {
        "id": 3,
        "question": (
            'How satisfied are you with the work you do each week, including the tasks, growth opportunities, and value you feel you contribute?'
        ),
        "feature": "job_satisfaction",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    # ========================================================
    # RISK TOLERANCE
    # ========================================================

    {
        "id": 4,
        "question": (
            'How comfortable would you be moving into a new role if it offered long-term growth but involved uncertainty during the transition?'
        ),
        "feature": "risk_tolerance",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # ========================================================
    # FINANCIAL FLEXIBILITY
    # ========================================================

    {
        "id": 5,
        "question": (
            'How prepared are you financially to cover essential expenses while studying, retraining, or searching for a new role?'
        ),
        "feature": "financial_flexibility",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # ========================================================
    # DOMAIN EXPERTISE DEPTH
    # ========================================================

    {
        "id": 6,
        "question": (
            'How confidently can you handle complex tasks that require specialist knowledge of your current professional domain?'
        ),
        "feature": "domain_expertise_depth",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # ========================================================
    # LEADERSHIP EXPERIENCE
    # ========================================================

    {
        "id": 7,
        "question": (
            'How much experience do you have setting priorities, mentoring colleagues, resolving team issues, or coordinating delivery?'
        ),
        "feature": "leadership_experience",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # ========================================================
    # NETWORKING STRENGTH
    # ========================================================

    {
        "id": 8,
        "question": (
            'How confidently can you contact people in your industry to learn about openings, get advice, or build useful professional relationships?'
        ),
        "feature": "networking_strength",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # ========================================================
    # DESIRE FOR STABILITY
    # ========================================================

    {
        "id": 9,
        "question": (
            'When considering a career move, how important are predictable hours, job security, and a steady income to you?'
        ),
        "feature": "desire_for_stability",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    # ========================================================
    # ENTREPRENEURIAL DRIVE
    # ========================================================

    {
        "id": 10,
        "question": (
            'How motivated are you to validate a business idea, find customers, and take responsibility for launching a service or product?'
        ),
        "feature": "entrepreneurial_drive",
        "type": "interest",
        "options": INTEREST_OPTIONS
    }

,

    {
        "id": 11,
        "question": 'How well can you explain the outcomes you have delivered in previous roles and the level of responsibility you have taken on?',
        "feature": "experience_level",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 12,
        "question": 'When you review job descriptions for a possible career move, how often can you demonstrate the required skills with examples from your work?',
        "feature": "current_skill_relevance",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 13,
        "question": 'How often does your current role provide meaningful challenges, recognition, and a realistic path for professional development?',
        "feature": "job_satisfaction",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 14,
        "question": 'How willing are you to test a new career direction through a small project, short course, or trial assignment before committing fully?',
        "feature": "risk_tolerance",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 15,
        "question": 'Could you manage your essential financial commitments if a transition required a period of lower earnings or additional training costs?',
        "feature": "financial_flexibility",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 16,
        "question": 'How well can you diagnose difficult work problems using the methods, tools, and subject knowledge of your current field?',
        "feature": "domain_expertise_depth",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 17,
        "question": 'How effectively have you helped a team deliver a project, resolve a disagreement, or make a decision under a deadline?',
        "feature": "leadership_experience",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 18,
        "question": 'How comfortable are you asking former colleagues, mentors, or industry contacts for feedback and information about other career paths?',
        "feature": "networking_strength",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 19,
        "question": 'How strongly would you prefer a stable role with clear expectations over a less predictable role with potentially faster growth?',
        "feature": "desire_for_stability",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 20,
        "question": 'How willing are you to take an idea beyond planning by testing demand, organising resources, and accepting responsibility for the result?',
        "feature": "entrepreneurial_drive",
        "type": "interest",
        "options": INTEREST_OPTIONS
    }
]


# ------------------------------------------------------------
# STAGE 3 HELPER FUNCTION
# ------------------------------------------------------------

def get_stage3_questions():
    """Return all Stage 3 career-switch assessment questions."""
    return STAGE3_QUESTIONS

# ============================================================
# STAGE 4 ASSESSMENT QUESTIONS
# Postgraduate - Next Career Step
# ============================================================

STAGE4_QUESTIONS = [

    # 1. Research Aptitude
    {
        "id": 1,
        "question": (
            'How confidently can you turn a broad topic in your postgraduate field into a focused research question that can be investigated?'
        ),
        "feature": "research_aptitude",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # 2. Publication Experience
    {
        "id": 2,
        "question": (
            'How much experience do you have preparing a literature review, thesis chapter, conference paper, manuscript, or research presentation?'
        ),
        "feature": "publication_experience",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # 3. Industry Internship Experience
    {
        "id": 3,
        "question": (
            'How effectively have you applied postgraduate knowledge during an industry internship, consultancy task, laboratory project, or placement?'
        ),
        "feature": "industry_internship_experience",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # 4. Leadership Interest
    {
        "id": 4,
        "question": (
            'How interested are you in managing a project team, setting priorities, and making decisions that affect a department or organisation?'
        ),
        "feature": "leadership_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    # 5. Technical Depth
    {
        "id": 5,
        "question": (
            'How confidently can you evaluate advanced methods, tools, or technical approaches and justify which is suitable for a specialist problem?'
        ),
        "feature": "technical_depth",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # 6. Teaching Interest
    {
        "id": 6,
        "question": (
            'How interested are you in teaching a subject related to your postgraduate specialisation, supervising learners, or supporting academic development?'
        ),
        "feature": "teaching_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    # 7. Risk Tolerance
    {
        "id": 7,
        "question": (
            'How comfortable are you choosing between research, industry, further study, or a venture when each option has uncertain outcomes?'
        ),
        "feature": "risk_tolerance",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # 8. Business Acumen
    {
        "id": 8,
        "question": (
            'How confidently can you assess the practical feasibility of a research-based product or service by considering users, costs, and market needs?'
        ),
        "feature": "business_acumen",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # 9. Patience for Long-Term Projects
    {
        "id": 9,
        "question": (
            'How willing are you to work through repeated experiments, revisions, or slow progress on a thesis or complex professional project?'
        ),
        "feature": "patience_for_long_term_projects",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    # 10. Industry Networking Strength
    {
        "id": 10,
        "question": (
            'How confidently can you build relationships with potential supervisors, researchers, employers, or specialists who could support your next step?'
        ),
        "feature": "networking_industry_strength",
        "type": "ability",
        "options": ABILITY_OPTIONS
    }

,

    {
        "id": 11,
        "question": 'How well can you compare research methods and evidence to decide whether they can answer a specific question in your field?',
        "feature": "research_aptitude",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 12,
        "question": 'How comfortable are you incorporating supervisor or reviewer feedback and revising academic work to meet publication standards?',
        "feature": "publication_experience",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 13,
        "question": "How effectively can you translate findings from an internship or applied project into recommendations that address an organisation's needs?",
        "feature": "industry_internship_experience",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 14,
        "question": 'How interested are you in leading a research group, coordinating a cross-functional project, or taking responsibility for project outcomes?',
        "feature": "leadership_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 15,
        "question": 'How well can you explain the limitations and trade-offs of advanced techniques used in your postgraduate specialisation?',
        "feature": "technical_depth",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 16,
        "question": 'How interested are you in designing a lesson, explaining a specialised concept, or mentoring junior students in your field?',
        "feature": "teaching_interest",
        "type": "interest",
        "options": INTEREST_OPTIONS
    },

    {
        "id": 17,
        "question": 'How comfortable are you pursuing a research or entrepreneurial opportunity when funding, results, or career outcomes are not guaranteed?',
        "feature": "risk_tolerance",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 18,
        "question": 'How well can you connect a technical or research idea to a user problem, an implementation plan, and the resources needed to deliver it?',
        "feature": "business_acumen",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 19,
        "question": 'How consistently can you sustain work on a long research or development project when results require many iterations?',
        "feature": "patience_for_long_term_projects",
        "type": "ability",
        "options": ABILITY_OPTIONS
    },

    {
        "id": 20,
        "question": 'How comfortable are you presenting your work at academic or professional events and following up to develop future collaborations?',
        "feature": "networking_industry_strength",
        "type": "ability",
        "options": ABILITY_OPTIONS
    }
]


# ------------------------------------------------------------
# STAGE 4 HELPER FUNCTION
# ------------------------------------------------------------

def get_stage4_questions():
    """Return all Stage 4 postgraduate career assessment questions."""
    return STAGE4_QUESTIONS