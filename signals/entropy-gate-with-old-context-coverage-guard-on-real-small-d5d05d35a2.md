# Entropy Gate with Old-Context Coverage Guard on Real Small-Model Attention Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `entropy-gate-with-old-context-coverage-guard-on-real-small-d5d05d35a2`
Run ID: `entropy-gate-with-old-context-coverage-guard-on-real-small-d5d05d35a2-20260524T030736264925+0000`

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

- Parent run decision: Entropy-Gated KV Eviction for CPU Long Context: enoch://control-plane/projects/entropy-gated-kv-eviction-for-cpu-long-context-70ba78e32f49/runs/entropy-gated-kv-eviction-for-cpu-long-context-70ba78e32f49-20260524T015313102764+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d24ceda12ad

## What looked useful

The old-context guard directly corrects the observed entropy-gate failure mode: unguarded entropy gating retained almost no old-heavy old-context mass, while the guard improved old-heavy old-context mass by +0.195 to +0.474 with positive paired bootstrap intervals. However, simple stride/heavy-hitter controls remain stronger at tight 10% budget and often retain more old-context mass.

## Boundaries and scale limits

Trace replay only; distilgpt2 and gpt2 only; sequence length at most 128; no physically truncated KV decoding, perplexity, task quality, latency, larger-model, longer-context, or guard-fraction sweep validation.

## Claim scope

On small GPT-2-family real attention traces, adding a 25% old-context coverage reserve to an entropy-gated fixed-budget KV selector substantially improves retained attention mass on old-heavy queries versus the unguarded entropy gate.

## Why it stopped

Tier 1 direct trace replay met the mechanism threshold but does not provide end-to-end decoding or quality evidence, so this remains no-paper useful signal.

## Recommended next action

Run a bounded truncated-KV decoding benchmark on the same small models comparing entropy gate plus old-context guard against stride/anchor-aware and heavy-hitter baselines on perplexity at equal KV budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Truncated-KV decoding check for entropy gate with old-context guard
- Success threshold: Guarded entropy gate must improve perplexity or NLL degradation versus unguarded entropy gate with a positive paired interval and be within 5% relative degradation of the best simple control, without more than 10% runtime overhead.
- Stop condition: Stop if guarded entropy gating fails to beat unguarded entropy gating on perplexity/NLL or remains clearly worse than stride/heavy-hitter controls at both 10% and 25% KV budgets.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gate-with-old-context-coverage-guard-on-real-small-d5d05d35a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
