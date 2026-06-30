# Real-model GB10 validation of token-budget cascade for long-context QA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-gb10-validation-of-token-budget-cascade-for-lon-ec1e56e57d`
Run ID: `real-model-gb10-validation-of-token-budget-cascade-for-lon-ec1e56e57d-20260609T121913572159+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Token-Budget Cascade for Long-Context Home Inference on gb10: enoch://control-plane/projects/token-budget-cascade-for-long-context-home-inference-on-gb10-98812a8100aa/runs/token-budget-cascade-for-long-context-home-inference-on-gb10-98812a8100aa-20260609T071555579853+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/153d62b5b21c

## What looked useful

The cascade matched full-context QA accuracy at 16/16 while reducing mean approximate input tokens from 3713 to 413; a front-truncated budget baseline reached only 6/16, indicating selection rather than token reduction alone drove the result.

## Boundaries and scale limits

Synthetic records, exact subject lexical cues, single-hop extraction, one main model, 8192-token runtime context, and no realistic benchmark or adversarial retrieval stress test.

## Claim scope

On 16 controlled synthetic single-hop long-context QA cases using Qwen2.5-7B-Instruct Q4_K_M on GB10, a lexical token-budget cascade preserved full-context accuracy while using 11.1% of approximate input tokens.

## Why it stopped

Tier 1 controlled direct test completed and produced a useful bounded mechanism signal, but evidence is not publication-grade because the corpus and selector are synthetic and favorable.

## Recommended next action

Run a bounded deepen test on realistic or adversarial multi-document QA with harder retrieval and the same full-context, cascade, and truncated-budget controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adversarial realistic QA validation of token-budget cascade
- Success threshold: Cascade accuracy is at least 95% of full-context accuracy, prompt-token ratio is at most 0.40, and front-truncated baseline remains at least 15 percentage points below cascade accuracy.
- Stop condition: Stop if cascade target recall falls below 80% after 20 cases or if token ratio exceeds 0.60 without an accuracy advantage over full context or truncation.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-gb10-validation-of-token-budget-cascade-for-lon-ec1e56e57d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
