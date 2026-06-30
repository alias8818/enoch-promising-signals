# LLM-in-the-loop operator-doctrine memory replay with noisy transcripts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-in-the-loop-operator-doctrine-memory-replay-with-noisy-e620dbd888`
Run ID: `llm-in-the-loop-operator-doctrine-memory-replay-with-noisy-e620dbd888-20260621T200336018897+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Operator-Doctrine Memory vs Flat Retrieval: Repeated-Task Agent Study: enoch://control-plane/projects/operator-doctrine-memory-vs-flat-retrieval-repeated-task-agent-study-d6fa9888eecf/runs/operator-doctrine-memory-vs-flat-retrieval-repeated-task-agent-study-d6fa9888eecf-20260621T194203093681+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/800ffea83752

## What looked useful

Layered doctrine memory reached 11/12 accuracy and helped on missing-doctrine/noisy-memory handling, but best simple baselines reached 10/12, so the predeclared +0.25 absolute-gain threshold was not met.

## Boundaries and scale limits

Synthetic JSONL corpus, rule-based extraction, no live LLM-in-the-loop execution, no private operator data, no embedding retrieval, and only 12 tasks; not publication-grade or broad validation.

## Claim scope

Tier 1 controlled direct test over 12 synthetic noisy operator-doctrine replay transcripts using deterministic retrieval strategies.

## Why it stopped

Controlled Tier 1 evidence produced useful mechanism signal but failed the stated improvement threshold; this is a no-paper mixed result, not a full validation.

## Recommended next action

Run a bounded deepen follow-up with condition-aware doctrine matching, paraphrased noise, and at least 48 controlled tasks; require a statistically meaningful gain over transcript_search and flat_retrieval before considering paper escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Condition-aware operator-doctrine memory replay under paraphrased noisy transcripts
- Success threshold: Condition-aware layered doctrine memory accuracy >= 0.85 and at least +0.15 absolute accuracy over the best non-layered baseline on >=48 tasks, with missing-doctrine default accuracy >= 0.90.
- Stop condition: Stop as finalize_negative if the gain over the best baseline is below +0.10 or ambiguous-boundary failures remain above 20%.

## Evidence references

- Artifact root: `<local-path>/projects/llm-in-the-loop-operator-doctrine-memory-replay-with-noisy-e620dbd888`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
