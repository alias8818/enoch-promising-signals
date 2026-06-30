# Speculative Cascade with Draft Model Warmed by Router Prefix

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-cascade-with-draft-model-warmed-by-router-prefix-e119cc702dd0`
Run ID: `speculative-cascade-with-draft-model-warmed-by-router-prefix-e119cc702dd0-20260528T054113510946+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b47b93fd62bd

## What looked useful

Router prefix improved mean acceptance from 0.5889 to 0.6769 versus no prefix on GPT-2/distilGPT-2, but generic prefix reached 0.7006 and wrong prefix was close at 0.6708. In the GPT-2/GPT-2 control, no prefix acceptance was 1.0000 while router prefix fell to 0.7607, showing draft-only prefixing is a conditioning mismatch in the clean case.

## Boundaries and scale limits

Tested GPT-2 and distilGPT-2 public causal LMs, 36 hand-written prompts across four domains, 16 proposed tokens per prompt per condition for the main run, and a 16-prompt identical-model control. No production serving stack, instruction-tuned models, learned router, soft-prefix optimization, batching, or end-to-end latency measurement.

## Claim scope

Local GPT-2-class speculative acceptance proxy: draft-only natural-language prefixes can improve acceptance for a weaker distilGPT-2 draft versus no prefix, but the effect is not router-specific and draft-only prefixing degrades acceptance when target and draft distributions are otherwise identical.

## Why it stopped

Moderate local proxy evidence is mixed: the main weaker-draft run shows a prefix benefit, but the benefit is not router-specific, and the identical-model control directly demonstrates that draft-only prefixing can reduce speculative acceptance through target/draft conditioning mismatch.

## Recommended next action

Stop this draft-only router-prefix variant as no-paper evidence; the only worthwhile next local test is a learned or optimized prefix that must beat generic and wrong-prefix controls on accepted-token throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Draft Prefix for Target Agreement in Speculative Decoding
- Success threshold: On held-out prompts, learned prefix improves accepted tokens per target forward pass and end-to-end tokens/second by at least 10% over the best of no-prefix, generic-prefix, and wrong-prefix controls, with unchanged target output distribution under exact speculative correction.
- Stop condition: Stop if the learned prefix fails to beat the best non-learned control by 10% on held-out accepted-token throughput, or if latency overhead from prefix handling erases the acceptance gain.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-cascade-with-draft-model-warmed-by-router-prefix-e119cc702dd0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
