# LLM-extracted evidence-ledger anchors on paraphrased episodic QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `llm-extracted-evidence-ledger-anchors-on-paraphrased-episo-0fdecf46ac`
Run ID: `llm-extracted-evidence-ledger-anchors-on-paraphrased-episo-0fdecf46ac-20260527T032143965757+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Online generative LLM-agent validation of minimal evidence-ledger anchors on episodic QA: enoch://control-plane/projects/online-generative-llm-agent-validation-of-minimal-evidence-1d9bdcf210/runs/online-generative-llm-agent-validation-of-minimal-evidence-1d9bdcf210-20260526T204621382864+0000
- Parent run decision: LLM agent validation of minimal evidence-ledger anchors on episodic QA: enoch://control-plane/projects/llm-agent-validation-of-minimal-evidence-ledger-anchors-on-07a4808ce0/runs/llm-agent-validation-of-minimal-evidence-ledger-anchors-on-07a4808ce0-20260526T142001330647+0000

## What looked useful

Canonical ledger anchors help paraphrased episodic evidence selection, but the clean-ledger gain over a straightforward tuned raw retriever was only +2.65 percentage points, below the predeclared +15 pp useful-signal threshold. An 8% slot-noise check remained high at 98.56% accuracy but still did not create a paper-ready margin over the strong baseline.

## Boundaries and scale limits

400,000 total QA instances across 5 fixed seeds for the main validation; synthetic templated narratives; deterministic extractor rather than an external LLM; no natural long-form corpus, dense retriever, or real LLM extraction-cost validation.

## Claim scope

On a controlled synthetic paraphrased episodic QA benchmark with deterministic slot extraction, evidence-ledger anchors achieve perfect exact-answer and anchor accuracy, beating weak raw BM25 and a randomized-action anchor ablation, but only modestly beating a synonym-expanded raw BM25 baseline.

## Why it stopped

Bounded direct validation found mechanism support but failed the material-improvement threshold over the strong raw-text baseline; this is not a full natural-corpus validation or publication-grade result.

## Recommended next action

Stop this branch as no-paper useful evidence; only reopen with a natural/semi-natural episodic QA dataset using actual LLM-extracted ledgers and a competitive hybrid retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual LLM-extracted evidence ledgers on natural episodic QA
- Success threshold: Ledger QA exact-answer accuracy and evidence retrieval accuracy each exceed the strongest retrieval baseline by at least 5 percentage points with no more than a 2 percentage point degradation under measured extractor noise.
- Stop condition: Stop if actual extraction slot/evidence accuracy is below 90%, or if ledger QA improvement over the strongest baseline is under 3 percentage points on a validation set of at least 1,000 questions.

## Evidence references

- Artifact root: `<local-path>/projects/llm-extracted-evidence-ledger-anchors-on-paraphrased-episo-0fdecf46ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
