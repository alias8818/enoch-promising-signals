# Gradient Coreset Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-coreset-tiny-pretraining-954ea4314cd5`
Run ID: `gradient-coreset-tiny-pretraining-954ea4314cd5-20260516T035636751344+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3920ac4291bd

## What looked useful

Gradient k-center selected rare regimes and improved rare-regime validation loss versus random, but worsened aggregate validation loss; naive top-loss/top-gradient selection failed badly. An oracle rare-balanced control matched most of the rare-regime benefit, suggesting the mechanism is diversity/rebalancing rather than a standalone gradient coreset win.

## Boundaries and scale limits

Proxy-only evidence: no real text corpus, no GPT-2-small-class model, no long training run, and no true full-parameter per-example gradient coreset.

## Claim scope

Synthetic motif-language tiny pretraining with a 2-layer 64-dim causal Transformer, 2048 training examples, 512 validation examples, 25% subset selection, 350 optimizer steps, and 3 seeds.

## Why it stopped

Proxy early falsification/mixed result: tested gradient coreset variants did not beat random subsets on aggregate validation loss, though gradient diversity improved rare-regime loss.

## Recommended next action

Stop this run as a no-paper proxy result; the concrete next bounded test is distribution-preserving gradient k-center with importance weighting on a small real text corpus against random and stratified controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distribution-Preserving Gradient Diversity Coresets on Real Tiny Text
- Success threshold: Weighted or stratified gradient k-center improves aggregate validation loss by at least 0.02 NLL versus random 25% subsets without worsening rare/high-loss-slice validation loss, replicated over at least 3 seeds.
- Stop condition: Stop if the weighted/stratified method still underperforms random on aggregate validation loss or if the rare-slice gain disappears under real-corpus controls.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-coreset-tiny-pretraining-954ea4314cd5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
