# Token-Level Loss Masking versus Sequence Dropping

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `token-level-loss-masking-versus-sequence-dropping-3a012f35d8bc`
Run ID: `token-level-loss-masking-versus-sequence-dropping-3a012f35d8bc-20260605T041201088681+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/05124460a93a

## What looked useful

Sequence dropping wasted clean signal as sequence length compounded sparse contamination: at 8% contamination it retained about 0.6% of available good-target transitions, while target masking retained clean targets and reduced clean held-out perplexity by about 7.6% relative to dropping. A stricter target-and-context mask nearly recovered the no-contamination baseline.

## Boundaries and scale limits

No transformer, real corpus, learned/noisy quality detector, tokenizer effects, downstream task metrics, or long training dynamics were tested. The result supports a mechanism, not a full LLM pretraining claim.

## Claim scope

In a synthetic Markov next-token modeling proxy with oracle token-quality labels, token-level target loss masking preserved recoverable clean-token supervision and achieved lower clean held-out NLL than dropping any sequence containing a contaminated token across five seeds and four nonzero contamination rates.

## Why it stopped

Synthetic proxy supports the mechanism but is not direct/full validation of token-level loss masking for real LLM training.

## Recommended next action

Stop this run as no-paper useful-signal evidence; run a bounded deepen follow-up with a small neural LM, matched token/compute budgets, realistic mixed-quality text, and non-oracle quality masks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Neural LM Validation of Token-Level Masking versus Sequence Dropping
- Success threshold: Masking must beat sequence dropping on clean held-out perplexity by at least 2% relative at equal compute in at least 4 of 5 seeds, with no worse downstream/robustness diagnostic beyond a predeclared tolerance.
- Stop condition: Stop if masking fails to beat dropping in 3 or more seeds, if gains disappear under non-oracle labels, or if the run exceeds a bounded local compute budget without checkpointed direct metrics.

## Evidence references

- Artifact root: `<local-path>/projects/token-level-loss-masking-versus-sequence-dropping-3a012f35d8bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
