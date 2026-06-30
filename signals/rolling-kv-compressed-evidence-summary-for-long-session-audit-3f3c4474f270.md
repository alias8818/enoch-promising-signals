# Rolling KV-Compressed Evidence Summary for Long Session Audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rolling-kv-compressed-evidence-summary-for-long-session-audit-3f3c4474f270`
Run ID: `rolling-kv-compressed-evidence-summary-for-long-session-audit-3f3c4474f270-20260525T021650875184+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8993b96b9aa6

## What looked useful

Rolling KV with enough slots achieved 1.0 value and support recall on 4,800 queries per condition with about 160 stored tokens, while a 1,600-token recent window recovered about 0.017-0.019 recall; a 30-slot KV ablation recovered 0.375 recall, confirming capacity sensitivity.

## Boundaries and scale limits

Tested only 60 synthetic sessions per condition, 600 turns per session, 80 fact slots per session, deterministic regex extraction, and no LLM answer generation or real production transcripts.

## Claim scope

On deterministic synthetic long-session audit workloads with schema-extractable evidence facts, a streaming rolling KV summary preserved final fact values and support ids at full-log recall while using far fewer retained tokens than full logs or a fixed recent-token window.

## Why it stopped

No-paper closure: this run provides a reproducible synthetic mechanism signal, but not direct real-session or LLM-in-the-loop evidence.

## Recommended next action

Run a bounded deepen test with model-based online extraction on real or high-fidelity audit transcripts and compare against retrieval plus rolling text-summary baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-extracted rolling KV audit memory on realistic long-session transcripts
- Success threshold: Rolling KV improves support-correct audit answer accuracy by at least 15 percentage points over recent-window truncation and is within 5 percentage points of retrieval-over-full-log while using less than 15% of full-log retained tokens.
- Stop condition: Stop if extraction precision or recall on realistic transcripts falls below 0.8, or if rolling KV fails to beat recent-window support-correct accuracy by at least 5 percentage points on the first 200 labeled audit questions.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-kv-compressed-evidence-summary-for-long-session-audit-3f3c4474f270`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
