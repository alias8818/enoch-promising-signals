# Direct LLM evidence-ledger versus free-form tool-use benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-llm-evidence-ledger-versus-free-form-tool-use-bench-ed29c3d1d6`
Run ID: `direct-llm-evidence-ledger-versus-free-form-tool-use-bench-ed29c3d1d6-20260629T161952033272+0000`

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

- Parent run decision: Evidence-Ledger Agent Loop Beats Free-Form CoT on Tool-Use Reliability: enoch://control-plane/projects/evidence-ledger-agent-loop-beats-free-form-cot-on-tool-use-reliability-97e97be6776c/runs/evidence-ledger-agent-loop-beats-free-form-cot-on-tool-use-reliability-97e97be6776c-20260629T160230499071+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65a9515b260a

## What looked useful

Ledger: balanced_accuracy=1.0, valid_accept_rate=1.0, parse_failures=0. Free form: balanced_accuracy=0.5, valid_accept_rate=0.0, parse_failures=294 across 120 cases, while invalid recall was 1.0 for both protocols.

## Boundaries and scale limits

No real LLMs, no live tools, no human-written traces, and no multi-domain benchmark were used. The benchmark tests protocol audit surface, not end-to-end model reliability or agent task success.

## Claim scope

Seeded local synthetic auditability proxy for machine-checking claim/evidence outputs. The result supports only that strict ledger structure improves parseability and valid-case acceptance versus a strict free-form citation extractor under citation-style variation.

## Why it stopped

Proxy-only evidence is useful but insufficient for a paper or broad benchmark claim; it does not validate real LLM behavior.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test the same paired protocol on real LLM outputs over hidden-drift tool-use tasks with identical evidence payloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM paired evidence-ledger versus free-form hidden-drift benchmark
- Success threshold: Ledger protocol improves balanced accuracy by at least 0.15 over free-form while not reducing invalid-claim recall, across at least 100 paired real-model task outputs.
- Stop condition: Stop if ledger parsing fails above 5%, if both protocols have balanced accuracy below 0.6, or if real-model access cannot be obtained without private credentials.

## Evidence references

- Artifact root: `<local-path>/projects/direct-llm-evidence-ledger-versus-free-form-tool-use-bench-ed29c3d1d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
