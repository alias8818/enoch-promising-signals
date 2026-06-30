# Length-Difficulty Balanced Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `length-difficulty-balanced-data-selection-for-tiny-pretraining-48d0635d3544`
Run ID: `length-difficulty-balanced-data-selection-for-tiny-pretraining-48d0635d3544-20260608T174925967853+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7039c70da27b

## What looked useful

In an imbalanced synthetic corpus, length-difficulty balanced selection reduced mean worst-cell validation loss by 0.2286 absolute, 4.92% relative to random, and achieved the best mean average validation loss across 3 seeds. This supports a bounded real-data follow-up but is not paper-ready.

## Boundaries and scale limits

No natural-language corpus, no learned or model-based real difficulty score, no Transformer/GPT-2-small-class baseline, no large-token pretraining, and no datacenter-scale validation. The length-axis contribution is small relative to difficulty-only in this proxy.

## Claim scope

Synthetic tiny causal-LM proxy with controlled length and difficulty bins, equal 95k-token selection budgets, 3 seeds, and a GRU language model; joint length-difficulty balancing improved balanced-validation average loss and worst-cell loss versus random, short/easy, and length-only selection, and was marginally better than difficulty-only selection.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy evidence, not direct publication-grade validation.

## Recommended next action

Run a bounded real-data tiny-Transformer follow-up using length bins plus reference-model-loss difficulty scores, and require joint balancing to beat random and both single-axis controls on worst-cell loss without average-loss regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data tiny-Transformer validation of length-difficulty balanced selection
- Success threshold: Joint length-difficulty balancing must reduce mean worst-cell validation loss by at least 2% relative to random and beat both single-axis controls, while changing mean average validation loss by no more than +0.5%.
- Stop condition: Stop as negative if joint balancing fails to beat either single-axis control on worst-cell loss or if it improves worst-cell loss only by worsening average validation loss beyond 0.5%.

## Evidence references

- Artifact root: `<local-path>/projects/length-difficulty-balanced-data-selection-for-tiny-pretraining-48d0635d3544`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
