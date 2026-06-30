# Human and LLM audit robustness on paraphrased real-trace ledger claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `88`
Project ID: `human-and-llm-audit-robustness-on-paraphrased-real-trace-l-75c2b4323c`
Run ID: `human-and-llm-audit-robustness-on-paraphrased-real-trace-l-75c2b4323c-20260611T084512033112+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `88`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Human/LLM natural-claim audit benchmark for real trace evidence ledgers: enoch://control-plane/projects/human-llm-natural-claim-audit-benchmark-for-real-trace-evi-94500e4a0b/runs/human-llm-natural-claim-audit-benchmark-for-real-trace-evi-94500e4a0b-20260611T061238894261+0000
- Parent run decision: Real-trace evidence ledger audit benchmark: enoch://control-plane/projects/real-trace-evidence-ledger-audit-benchmark-2ea74178ab/runs/real-trace-evidence-ledger-audit-benchmark-2ea74178ab-20260611T055221843457+0000

## What looked useful

Full-trace bounded validation found that DistilBERT MNLI and FLAN-T5-small accepted true paraphrases with >99% accuracy and <1% paraphrase flip rates, but rejected only 6.74% and 3.68% of corrupted ledger claims respectively. A structured parser control reached 98.15% overall accuracy and 96.30% false-control accuracy, showing the task is locally checkable while naive neural auditors are not reliable.

## Boundaries and scale limits

No human subjects were evaluated, and no frontier or tool-using LLMs were tested. Paraphrases were deterministic template paraphrases rather than human-authored paraphrases. The numeric parser control is tailored to generated claim forms and is a structured verification control, not a general natural-language auditor.

## Claim scope

All 6,567 rows of the public MoneyData anonymized bank-transaction workbook were converted into true canonical claims, true paraphrases, and false controls for amount, category, direction, and ending balance. In this scoped benchmark, off-the-shelf local small neural auditors were stable across true paraphrases but failed as auditors because they accepted most corrupted claims.

## Why it stopped

Bounded full real-trace validation directly falsified the strongest local claim that off-the-shelf small LLM/NLI auditors robustly audit paraphrased ledger claims: they were paraphrase-stable but accepted most false controls.

## Recommended next action

Stop this follow-up as a no-paper useful signal; a publishable next stage would need actual human-subject audit data and stronger tool-using/frontier LLM baselines on the same claim set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human and tool-using LLM audit comparison on MoneyData ledger claim controls
- Success threshold: On a heldout fixed-seed set of at least 1,000 claim instances, each auditor must achieve >=90% true-paraphrase accuracy, >=90% false-control rejection, and <=5% paraphrase flip rate; report confidence intervals and corruption-type breakdowns.
- Stop condition: Stop if human evidence cannot be obtained or if tool-using/frontier LLM baselines fail to exceed 80% false-control rejection while preserving >=90% true-paraphrase accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/human-and-llm-audit-robustness-on-paraphrased-real-trace-l-75c2b4323c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
