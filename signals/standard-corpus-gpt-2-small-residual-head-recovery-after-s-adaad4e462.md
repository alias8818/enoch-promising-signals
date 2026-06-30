# Standard-corpus GPT-2-small residual-head recovery after sub-2-bit ternary quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `standard-corpus-gpt-2-small-residual-head-recovery-after-s-adaad4e462`
Run ID: `standard-corpus-gpt-2-small-residual-head-recovery-after-s-adaad4e462-20260620T010959873400+0000`

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

- Parent run decision: Sub-2-bit forward with logit-domain residual head: enoch://control-plane/projects/sub-2-bit-forward-with-logit-domain-residual-head-a39fba6720ff/runs/sub-2-bit-forward-with-logit-domain-residual-head-a39fba6720ff-20260620T003115813632+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b77064485f94

## What looked useful

The dense output head recovered 20.3% of the NLL damage at threshold factor 0.7 but still had perplexity 69,185 versus 31.6 dense; threshold sensitivity recovered -9.5%, 0.8%, and 6.7% at factors 0.3, 0.5, and 1.0.

## Boundaries and scale limits

Single standard-corpus slice, no calibrated quantization, no retraining, no full WikiText-2 pass, no alternate corpora, and no residuals outside the output head.

## Claim scope

GPT-2-small on a 32,704-token WikiText-2 validation slice with naive per-tensor ternary quantization of all 2D parameters: restoring only a dense untied lm_head residual does not recover usable language-model quality.

## Why it stopped

Direct Tier 1 GPT-2-small standard-corpus evidence falsified output-head-only residual recovery as a practical repair for naive sub-2-bit ternary quantization; this is not a full-scale validation of all quantization methods.

## Recommended next action

Stop this output-head-only line as no-paper evidence; if continuing locally, test a bounded residual-scope localization follow-up covering input embedding plus final transformer block residuals under the same WikiText-2 metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-scope localization for sub-2-bit ternary GPT-2-small recovery
- Success threshold: At least one bounded residual scope recovers >=50% of NLL damage versus ternary_all and reduces perplexity by >=10x relative to ternary_all without restoring more than 20% of model parameters densely.
- Stop condition: Stop as negative if embedding and final-block residual scopes both recover <50% of NLL damage on the 32,704-token WikiText-2 slice at two threshold factors.

## Evidence references

- Artifact root: `<local-path>/projects/standard-corpus-gpt-2-small-residual-head-recovery-after-s-adaad4e462`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
