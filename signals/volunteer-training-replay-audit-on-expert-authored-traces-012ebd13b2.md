# Volunteer Training Replay Audit on Expert-Authored Traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `volunteer-training-replay-audit-on-expert-authored-traces-012ebd13b2`
Run ID: `volunteer-training-replay-audit-on-expert-authored-traces-012ebd13b2-20260613T132750633021+0000`

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

- Parent run decision: Spot-Check Volunteer Training: Deterministic Replay Audit: enoch://control-plane/projects/spot-check-volunteer-training-deterministic-replay-audit-0f8cb1b3f121/runs/spot-check-volunteer-training-deterministic-replay-audit-0f8cb1b3f121-20260613T124149387972+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f83ebaa4f43d

## What looked useful

Layered doctrine memory did not beat transcript_search or flat_retrieval on the controlled set: all three scored 11/12 accuracy with 0.0833 decoy-hit rate. The set is too lexically easy for layered memory to separate from simpler retrieval, and the shared failure identifies a missing/no-label condition-normalization gap.

## Boundaries and scale limits

No live LLM answerer, no real human transcript corpus, no confidence intervals, and no large held-out curriculum; evidence is limited to a small CPU-only deterministic replay set.

## Claim scope

Controlled small direct replay audit on 12 expert-authored volunteer-training traces comparing deterministic no-memory, transcript-search, flat-retrieval, and layered-doctrine-memory strategies.

## Why it stopped

Tier 1 direct controlled threshold was falsified: layered accuracy minus best non-layered baseline was 0.0 rather than >= 0.20, so this is useful no-paper evidence rather than paper-positive support.

## Recommended next action

Run a bounded adversarial paraphrase-condition replay follow-up that stresses negation, absent/missing labels, and semantically equivalent conditions before spending effort on larger volunteer-training traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adversarial condition-normalization replay for volunteer-training memory
- Success threshold: Condition-normalized layered memory beats the best non-layered baseline by >= 0.15 accuracy and keeps decoy_hit_rate <= 0.10 on adversarial condition tasks.
- Stop condition: Stop if transcript_search or flat_retrieval remains within 0.05 accuracy of the best layered variant, or if layered gains come only from task-specific keyword rules.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-training-replay-audit-on-expert-authored-traces-012ebd13b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
