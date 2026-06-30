# Token-level residual-channel sub-2-bit validation against equal-memory baselines

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `token-level-residual-channel-sub-2-bit-validation-against-21fa3aba48`
Run ID: `token-level-residual-channel-sub-2-bit-validation-against-21fa3aba48-20260613T211301962583+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Sub-2-bit weights with per-layer learned residual channels: enoch://control-plane/projects/sub-2-bit-weights-with-per-layer-learned-residual-channels-543bd4d49e6e/runs/sub-2-bit-weights-with-per-layer-learned-residual-channels-543bd4d49e6e-20260613T200151956251+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/63c9cb3c594b

## What looked useful

Residual-channel top-k produced strong reconstruction metrics but failed the target predictive metric: across three controlled seeds it increased NLL by 19.64-22.62%, while a 1.021-bit dense sign residual baseline increased NLL by only 7.23-8.05%.

## Boundaries and scale limits

No intermediate-layer injection, no training-loop validation, no larger GPT-2-small/full or 7B+ model, no long-context evaluation, and no deployed entropy-coded/kernel implementation. The result is an early falsification of this final-hidden-state codec formulation, not a universal impossibility proof.

## Claim scope

Tier 1 direct test on distilgpt2 final hidden states from Wikitext-2 validation chunks: the tested token-level residual-channel top-k codec at 1.496 bits per scalar did not preserve next-token NLL better than a lower-memory dense sign residual baseline.

## Why it stopped

Tier 1 direct test falsified the preregistered threshold for the tested residual-channel formulation: it was sub-2-bit but exceeded 10% NLL degradation and lost to a lower-memory baseline. This is an early direct falsification, not a full validation across model scales.

## Recommended next action

Stop this residual-channel top-k branch as no-paper evidence; run a separate bounded branch validating dense sign residual coding across intermediate layers and a GPT-2-small-class model.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Dense sign residual sub-1.1-bit validation across residual layers
- Success threshold: At less than or equal to 1.1 bits per scalar, dense sign residual coding keeps NLL degradation below 10% and beats all equal-or-higher-memory baselines on NLL in every tested layer/seed setting.
- Stop condition: Stop if dense sign residual coding exceeds 10% NLL degradation or loses NLL to an equal/lower-memory baseline in two independent seeds or layers.

## Evidence references

- Artifact root: `<local-path>/projects/token-level-residual-channel-sub-2-bit-validation-against-21fa3aba48`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
