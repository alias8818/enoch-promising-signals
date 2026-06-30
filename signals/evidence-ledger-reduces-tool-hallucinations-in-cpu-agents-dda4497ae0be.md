# Evidence Ledger Reduces Tool Hallucinations in CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-reduces-tool-hallucinations-in-cpu-agents-dda4497ae0be`
Run ID: `evidence-ledger-reduces-tool-hallucinations-in-cpu-agents-dda4497ae0be-20260523T053904416450+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1a2919369805

## What looked useful

On 20,000 synthetic tasks, baseline unsupported tool-claim rate was 27.12% versus 2.21% with the evidence ledger, an absolute reduction of 24.91 percentage points with bootstrap 95% CI [24.62, 25.19]. Across 18 sensitivity cases, all CIs excluded zero and the minimum absolute reduction was 16.18 percentage points.

## Boundaries and scale limits

No live LLM agents, no real shell/tool traces, no human evaluation, and no full agent-framework integration were tested. The result is a mechanism-level proxy and should not be treated as publication-grade validation of real CPU agents.

## Claim scope

In a deterministic synthetic CPU-agent transcript simulator, final reports constrained to cite an explicit tool-event evidence ledger had much lower unsupported tool-claim rates than baseline reports generated from intended actions plus noisy memory.

## Why it stopped

Stopped after a synthetic mechanism confirmation because broader scientific closure requires direct live-agent evidence; this is useful no-paper evidence rather than a full validation.

## Recommended next action

Run a bounded live-agent follow-up using real local CPU-agent tool traces, randomized baseline versus ledger reporting, and deterministic auditing against actual event logs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live CPU-Agent Evidence-Ledger Audit
- Success threshold: Unsupported tool-claim rate is reduced by at least 50% with bootstrap 95% CI excluding zero, while verified useful claim count drops by no more than 15% and task completion is not worse by more than 5 percentage points.
- Stop condition: Stop if the ledger condition fails to reduce unsupported claims by 25% in the first 50 audited traces or if verified useful claim coverage falls by more than 30%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-reduces-tool-hallucinations-in-cpu-agents-dda4497ae0be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
